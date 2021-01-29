import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import websocketapi.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro.settings.dev')
django.setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(

        )
    )
})
