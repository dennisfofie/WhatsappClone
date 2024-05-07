from rest_framework import serializers
from whatsappServiceApi.models import User, ResetPassword


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","email", "fullName", "password", "profilePic", "active", "created", "createdBy", "modified", "modifiedBy"]

        read_only_fields = ['active', 'id', 'createdBy', 'modifiedBy']
        write_only_fields = ['password']

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profilePic']

        read_only_fields = ['profile', 'fullName']


class ResetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResetPassword
        fields = ['oldPassword', 'newPassword', 'confirmPassword']

