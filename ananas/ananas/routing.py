from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import messenger.routing
from channels.security.websocket import AllowedHostsOriginValidator

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
    	AuthMiddlewareStack(
        	URLRouter(
            	messenger.routing.websocket_urlpatterns
        	)
    	),
    )
})