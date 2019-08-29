from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/mynotes', consumers.NoteConsumer)
]