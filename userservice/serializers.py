from rest_framework import serializers

from .models import UserService


class UserServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserService
        fields = ["user1", "user2", "service1", "service2"]
