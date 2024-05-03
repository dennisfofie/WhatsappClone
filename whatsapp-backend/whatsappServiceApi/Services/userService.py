from whatsappServiceApi.models import User, ResetPassword
from whatsappServiceApi.Services.userDatabaseService import UserDatabaseService

from whatsappServiceApi.Serializers.userSerializers import (
    RegistrationSerializer,
    LoginSerializer,
    ResetPassword
)

from whatsappServiceApi.Helpers.standardPagination import StandardResultsSetPagination

from whatsappServiceApi.Helpers.tokens import generate_tokens

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.settings import api_settings

import json
from django.contrib.auth.hashers import make_password
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

class UserApplicationService(viewsets.GenericViewSet):
    pagination_class = StandardResultsSetPagination
    lookup_url_kwarg='userId'
    userDb = None
    serializer_class = RegistrationSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.userDb = UserDatabaseService()

    @staticmethod
    def __createResponse(data, httpStatus):
        return Response(json.loads(json.dumps(data)), httpStatus)
    

    def create(self, request:Request):
        try:
            email = request.data.get('email')
            fullname = request.data.get('fullName')
            password = request.data.get('password')

            message = ""


            if email is None or email == "":
                message += "email must be provided it is required "
            
            
            if fullname is None or fullname == "":
                message += " and Full name must be provided and it is required"

                return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
            
            if len(password) < 8 or password is None:
                data = "password must be greater than 8 and alpha numeric"
                return self.__createResponse(data, status.HTTP_400_BAD_REQUEST)
            
            encodedPassword = make_password(password)

            #TODO: save the profile to amazon s3 bucket

            user = User(
                email = email,
                fullName = fullname,
                password = encodedPassword,
            )

            result = self.userDb.CreateUser(user)

            if result is None:
                message = {"Error": "Error occurred while creating user"}
                return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
            
            # activating user
            activatedUser = self.userDb.Activate(result.userId)

            if None == activatedUser:
                message = {"Error": "Error occurred while activating user"}

                return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
            

            #assigning tokens to user
            tokens = generate_tokens(activatedUser)

            if tokens is None:
                message = {"Error": "Error occurred while creating user tokens"}
            
            serializer = self.serializer_class(activatedUser, many=False)

            response = {
                    "access_token": tokens['access'],
                    "refresh": tokens['refresh'],
                    "data": serializer.data,
                }

            return self.__createResponse(response, status.HTTP_201_CREATED)
        except Exception as e:
            message = {"Error": "Unexpected error occurred while creating user"}
            return self.__createResponse(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        






