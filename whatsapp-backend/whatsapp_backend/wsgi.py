import os
from dotenv import load_dotenv

load_dotenv()

from django.core.wsgi import get_wsgi_application

PROJECT_NAME = os.getenv('PROJECT_NAME')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME+'whatsapp_backend.settings.prod')

application = get_wsgi_application()
