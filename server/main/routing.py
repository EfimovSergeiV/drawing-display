from django.urls import path
from main.consumers import MyWebSocketConsumer

websocket_urlpatterns = [
    path('ws/api/', MyWebSocketConsumer.as_asgi()),
]