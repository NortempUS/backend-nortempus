from django.shortcuts import render

from .models import Service
from rest_framework.decorators import api_view, permission_classes

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ServiceSerializer

from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
