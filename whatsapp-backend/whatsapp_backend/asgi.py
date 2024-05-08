import os
from dotenv import load_dotenv

load_dotenv()

from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from whatsappServiceApi.Services.messageConsumer import MessageConsumer


PROJECT_NAME = os.getenv('PROJECT_NAME')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings.prod')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter([
                    path("chat", MessageConsumer.as_asgi()),
                ])
            )
        )
    }
)
