from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import ChatAdmin.routing

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            ChatAdmin.routing.websocket_urlpatterns
        )
    )
})