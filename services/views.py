from django.shortcuts import render

from category.models import Category

from .models import Service
from rest_framework.decorators import api_view, permission_classes

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ServiceSerializer

from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_services(request):
    category_names = []
    services = Service.objects.all()
    for service in services:
        category_names.append(service.category.category_type)
    serializer = ServiceSerializer(services, many=True)

    return Response(
        {"serializer": serializer.data, "category_names": category_names},
        status=status.HTTP_200_OK,
    )
