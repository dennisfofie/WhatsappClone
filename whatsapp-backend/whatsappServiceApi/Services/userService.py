from whatsappServiceApi.models import User, ResetPassword
from whatsappServiceApi.Services.userDatabaseService import UserDatabaseService

from whatsappServiceApi.Serializers.userSerializers import (
    RegistrationSerializer,
    LoginSerializer,
    ResetSerializer,
    ProfilePicSerializer
)

from whatsappServiceApi.Helpers.standardPagination import StandardResultsSetPagination

from whatsappServiceApi.Helpers.tokens import generate_tokens

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


import json
from django.contrib.auth.hashers import make_password, check_password

class UserApplicationService(viewsets.GenericViewSet):
    pagination_class = StandardResultsSetPagination
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    lookup_url_kwarg='userid'
    userDb = None
    serializer_class = RegistrationSerializer
    queryset = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.userDb = UserDatabaseService()

    @staticmethod
    def __createResponse(data, httpStatus):
        return Response(json.loads(json.dumps(data)), httpStatus)
    

    @action(
            methods=['post'],
            detail=False,
            url_path='register',
            serializer_class=RegistrationSerializer,
            permission_classes=[AllowAny]
    )
    def register_user(self, request:Request):
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
            print(result)

            if result is None:
                message = {"Error": "Error occurred while creating user"}
                return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
            
            # activating user
            activatedUser = self.userDb.Activate(result.id)

            if None == activatedUser:
                message = {"Error": "Error occurred while activating user"}

                return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
            
            print(f"Activated: user {activatedUser}")
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
        
    def list(self, request:Request):
        searchTerm = None
        print(request.user)
        print(request.META)

        if "search" in request.query_params:
            searchTerm = request.query_params.get("search")
        
        result = self.userDb.GetAllUser(searchTerm)

        if result is None:
            data = {
                "count":0,
                "prev": None,
                "next": None,
                "result": []
            }

            return self.__createResponse(data, status.HTTP_204_NO_CONTENT)
        
        page = self.paginate_queryset(result)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)
        
        serializer = self.serializer_class(result, many=True)

        return self.__createResponse(
            serializer.data,
            status.HTTP_200_OK
        )
    
    def retrieve(self, request, userid=None):
        if userid is None:
            message = {
                "Error": "userId must be specified"
            }
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        result = self.userDb.GetUser(userid)

        if result is None:
            message = {
                "Error":
                "No account found with the provided userId"
            }
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.serializer_class(
            instance=result,
            many=False
        )

        return self.__createResponse(
            serializer.data,
            status.HTTP_200_OK
        )
    
    @action(
            methods=['put'],
            detail=True,
            url_path='update-pic',
            serializer_class=ProfilePicSerializer,
            permission_classes = [AllowAny]
    )
    def update_profilePicture(self, request, userid=None):
        
        profilePic = request.data.get("profilePic")

        if userid is None:
            message = {
                "Error": "Userid must be specified"
            }
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        user = self.userDb.GetUser(userid)

        if user is None:
            message = {
                "Error": "user account provided does not exist"
            }

            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        result = self.userDb.ChangePic(user.id, profilePic)

        if result is None:
            message = {
                "Error": "Changing of user profile picture failed"
            }

            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        serializer = self.serializer_class(
            result,
            many=False
        )

        response = {
            "message": "Profile image updated sucessfully",
            "data": serializer.data
        }

        return self.__createResponse(
            response,
            status.HTTP_201_CREATED
        )
    

    @action(
            methods=['get'],
            detail=True,
            url_path="deactivate",
            serializer_class=RegistrationSerializer
    )
    def deactivate_user(self, request, userid=None):

        if userid is None:
            message = {
                "Error": "Userid must be specified"
            }
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        result = self.userDb.Deactivate(userid)

        if result is None:
            message = {
                "Error": "An error occurred while deactiving user"
            }
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.serializer_class(
            result, many=False
        )

        response = {
            "message": "User account is deactivated",
            "data": serializer.data
        }

        return self.__createResponse(
            response,
            status.HTTP_200_OK
        )
    

    def update(self, request, userid):
        print(f"request: {request.data}")
     
        if userid is None:
            message = {
                "Error": "Userid must be specified"
            }
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )

        result = User.objects.get(id=userid)
        print(f"result: {result}")

        if result is None:
            message = {
                "Error": "User with specified id not found"
            }

        serializer = ProfilePicSerializer(instance=result,
            data=request.data, many=False, partial=True
        )

        print(f"serializer: {serializer}")

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return self.__createResponse(
                serializer.data,
                status.HTTP_201_CREATED
            )
        else:
            return self.__createResponse(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )
    
    @action(
            methods=['post'],
            detail=False,
            url_path='login',
            serializer_class= LoginSerializer,
            permission_classes=[AllowAny]
    )
    def login_user(self, request):

        print("login is starting")
        email = request.data.get("email")
        
        print(request.META)
        print(request.user)

        password = request.data.get("password")

        try:
            user = self.userDb.GetUserByEmail(email)
            print(user)
        except Exception as e:
            message = {
                "Error":"Invalid credentials"
            }

            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        print(request.user)

        if user is None:
            message = {
                "Error":"Invalid credentials"
            }

            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        userPassword = user.password

        if not check_password(password, userPassword):
            message = {
                "Error":"Invalid credentials"
            }

            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        tokens = generate_tokens(user)


        serializer = self.serializer_class(
            user, many=False
        )
        response = {
            "access_token":tokens['access'],
            "refresh": tokens['refresh'],
            "data": serializer.data['email']
        }

        return self.__createResponse(
            response,
            status.HTTP_200_OK
        )
    

    @action(
            methods=['put'],
            detail=True,
            url_path='reset',
            serializer_class=ResetSerializer,
            permission_classes=[AllowAny]
    )
    def reset_password(self, request, userid=None):
        if userid is None:
            message = {'Error': 'User with userId not found'}
            return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
        
        user = self.userDb.GetUser(userid)

        if user is None:
            message = {'Error': 'User with userId not found'}
            return self.__createResponse(message, status.HTTP_400_BAD_REQUEST)
        
        oldPassword = request.data.get("oldPassword")
        newPassword = request.data.get("newPassword")
        confirmPassword = request.data.get("confirmPassword")

        if oldPassword is None or oldPassword is "":
            message = {"Error": "Old password cannot be None"}
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        if not newPassword or not confirmPassword:
            message = {"Error": "New password must be provided"}
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        if not (newPassword == confirmPassword):
            message = {"Error": "New and Confirm password must be equal"}
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )
        
        if (len(newPassword) < 8 or not (newPassword.isalnum()) or 
            not (confirmPassword.isalnum())):
            message = {"Error": "Password must be alpha numeric"}
            return self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )

        reset = ResetPassword(
            resetUser = user,
            oldPassword = oldPassword,
            newPassword = newPassword,
            confirmPassword = confirmPassword
                )

        if reset is None:
            message = {"Error": "Failed to reset password"}
            self.__createResponse(
                message,
                status.HTTP_400_BAD_REQUEST
            )

        if check_password(oldPassword, user.password):
            if (newPassword != confirmPassword):
                return self.__createResponse(
                    {"Error": "Incorrect password"},
                    status.HTTP_400_BAD_REQUEST
                )
            else:
                self.userDb.ResetPassword(user, reset)
                user.password = make_password(newPassword)
                user.save()

        message = {"sucess": "User password updated sucessfully"}

        return self.__createResponse(
            message,
            status.HTTP_200_OK
        )
                
        

            


        
        


    

    









