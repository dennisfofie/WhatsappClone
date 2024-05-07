from whatsappServiceApi.models import Room, Message
from whatsappServiceApi.Serializers.userSerializers import RegistrationSerializer

from rest_framework import serializers

class CreateRoomSerializer(serializers.ModelSerializer):
    users = RegistrationSerializer(many=True)

    class Meta:
        model = Room
        fields = ['roomId', 'roomName', 'creator', 'icon', 'users', 'modified', 'created', 'ModifiedBy']
        depth=1
        write_only_fields = ['roomName']


class RoomSerializer(serializers.ModelSerializer):
    users = RegistrationSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'

class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        write_only_fields = [
            'chats',
            'audio',
            'image'
        ]

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'