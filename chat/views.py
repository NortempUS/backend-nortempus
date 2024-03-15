# Create your views here.

from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chatmess.models import ChatMess
from chatmess.serializers import ChatMessSerializer

from .models import Chat
from .serializers import ChatSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chats_by_user(request, user_id):
    try:
        chats = Chat.objects.filter(Q(user1=user_id) | Q(user2=user_id))
    except Chat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chat_by_id(request, chat_id):
    try:
        chat = Chat.objects.get(pk=chat_id)
        chatmess = ChatMess.objects.filter(chat=chat_id)
    except Chat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ChatMessSerializer(chatmess, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
