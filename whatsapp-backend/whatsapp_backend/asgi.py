import os
from dotenv import load_dotenv

load_dotenv()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator


PROJECT_NAME = os.getenv('PROJECT_NAME')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings.prod')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
    }
)
