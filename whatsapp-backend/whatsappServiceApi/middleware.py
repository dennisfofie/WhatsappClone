# from typing import Any
# import jwt
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from rest_framework.permissions import IsAdminUser

# User=get_user_model()


# class JWTMiddleware:
#     secret = None
#     algorithms = None

#     def __init__(self, hello):
#         self.hello = hello
#         self.secret = settings.SECRET_KEY
#         self.algorithms = ['HS256']

#     def __call__(self, request):

#         self.decode_jwt(request)
#         return self.hello(request)
    
#     def decode_jwt(self, request):
#         print(request)

#         if request.META.get("HTTP_AUTHORIZATION") is not None:
#             token = request.META.get("HTTP_AUTHORIZATION").split(" ")[1]
#         else:
#             return

#         print(self.algorithms)
#         decoded = jwt.decode(
#             token, self.secret, self.algorithms
#         )


#         user_id = decoded['user_id']
        


#         obtained_user = User.objects.get(pk=user_id)


#         print(obtained_user.user_permissions)
#         print(request.user)

#         if object is not None:
#             print()
            
#         return obtained_user

# import asyncio

# class JWTMiddleware:
    
#     def __init__(self, get_response):
#         self.get_response = get_response

#     async def __call__(self, scope, receive, send):
#         print(dict(scope.get('headers', [])))
#         user = await scope['query_string']
#         print(user)
#         asyncio.sleep(3)

#         return await self.get_response(scope, receive, send)
    

class JWTMiddleware:
    pass