# from django.urls import path

from django.urls import path
from . import consumers
from . import views
urlpatterns = [
    path('', views.chat_view, name='chat'),  # Default view for the chat app
]
websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
