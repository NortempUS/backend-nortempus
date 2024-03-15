from rest_framework import serializers

from .models import ChatMess


class ChatMessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMess
        fields = ["chat", "user", "message", "timestamp"]
