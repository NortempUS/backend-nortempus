from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ChatMess
from users.models import CustomUser
from .serializers import ChatMessSerializer

# Create your views here.


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_chatmess(request, chat_id):
    print(request.data)
    serializer = ChatMessSerializer(data=request.data)

    if serializer.is_valid():
        chat_mess_instance = serializer.save()

        # Asigna el usuario actualmente autenticado a la instancia del chat mess
        chat_mess_instance.user = request.user

        # Asigna la marca de tiempo actual
        chat_mess_instance.timestamp = datetime.now()

        # Guarda la instancia del chat mess en la base de datos
        chat_mess_instance.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_chatmess_by_chat(request, chat_id):
    try:
        chat_mess = ChatMess.objects.filter(chat=chat_id)
    except ChatMess.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ChatMessSerializer(chat_mess, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
