from channels.generic.websocket import JsonWebsocketConsumer
from channels.layers import channel_layers

import jwt
import json
from django.conf import settings

from whatsappServiceApi.Serializers.messageSerializers import (
    MessageSerializer,
    CreateMessageSerializer,
)

from whatsappServiceApi.models import Message, User

from whatsappServiceApi.Services.messageDatabaseService import MessageDatabaseService

from whatsappServiceApi.Services.userDatabaseService import UserDatabaseService


class MessageConsumer(JsonWebsocketConsumer):
    secret_key = None
    auth_header = None
    algorithm = None
    messageDb = None
    userDb = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secret_key = settings.SECRET_KEY
        self.auth_header = str(settings.SIMPLE_JWT.get("AUTH_HEADER_TYPES")[0])
        self.algorithm = [settings.SIMPLE_JWT.get('ALGORITHM', [])]
        self.messageDb = MessageDatabaseService()
        self.userDb = UserDatabaseService()

    
    def connect(self):
        if self.get_user(self.scope) is None:
            self.close()
        else:
            self.scope['user'] = self.get_user(self.scope)
            print(self.scope['user'].email)
            self.accept()

        self.accept()


    def disconnect(self, code):
        self.close(code)



    def receive_json(self, content, **kwargs):
        self.send(content)


    def send_message(self, event):
        data = json.loads(event.data)
        print(data)

    def clean_bytes(self, file):
        pass



    def get_user(self, scope):
        headers = dict(scope.get("headers", {}))

        authorization = headers.get(b'authorization').decode('utf-8').split(" ")

        if len(authorization) != 2 or (authorization[0] != self.auth_header):
            return None
        
        token_decoded = self.decode_tokens(
            authorization[1],
            self.secret_key,
            self.algorithm
        )

        return self.userDb.GetUser(token_decoded.get("user_id"))
    

    def decode_tokens(self, tokens, secret, algorithm):
        
        decoded_token = {}

        try:
            decoded_token = jwt.decode(tokens, secret, algorithm)
        except jwt.DecodeError as err:
            pass

        return decoded_token
  