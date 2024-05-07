from channels.generic.websocket import AsyncWebsocketConsumer, JsonWebsocketConsumer
from channels.layers import channel_layers

class MessageConsumer(JsonWebsocketConsumer):
    pass