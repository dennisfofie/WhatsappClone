
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView, TokenObtainPairView)

from whatsappServiceApi.Services.userService import UserApplicationService

router = DefaultRouter()
router.register(r"users", UserApplicationService, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('token-refresh', TokenRefreshView.as_view()),
    path('token-verify', TokenVerifyView.as_view()),
]
