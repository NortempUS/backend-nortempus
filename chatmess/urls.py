from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("chat/chat/<int:chat_id>/create/", views.create_chatmess),
]
