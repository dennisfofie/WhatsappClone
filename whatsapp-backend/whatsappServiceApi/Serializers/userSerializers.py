from rest_framework import serializers
from whatsappServiceApi.models import User, ResetPassword


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["userId","email", "fullName","password", "profilePic", "active", "created", "createdBy", "modified", "modifiedBy"]

        read_only_fields = ['active', 'userId', 'createdBy', 'modifiedBy']
        write_only_fields = ['password']

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

class ResetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResetPassword
        fields = ['user']