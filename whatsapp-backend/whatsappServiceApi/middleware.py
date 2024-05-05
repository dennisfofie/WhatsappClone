from typing import Any
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model

User=get_user_model()


class JWTMiddleware:
    secret = None
    algorithms = None

    def __init__(self, get_response):
        self.get_response = get_response
        self.secret = settings.SECRET_KEY
        self.algorithms = ['HS256']

    def __call__(self, request):

        self.decode_jwt(request)
        return self.get_response(request)
    
    def decode_jwt(self, request):
        print(request.META)

        if request.META.get("HTTP_AUTHORIZATION") is not None:
            token = request.META.get("HTTP_AUTHORIZATION").split(" ")[1]
        else:
            return

        print(self.algorithms)
        decoded = jwt.decode(
            token, self.secret, self.algorithms
        )


        user_id = decoded['user_id']


        obtained_user = User.objects.get(pk=user_id)

        if object is not None:
            print(obtained_user)
        return obtained_user
