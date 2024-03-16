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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_services_by_receiver_id(request, id):
    category_names = []
    services = Service.objects.filter(receiver=id)
    for service in services:
        category_names.append(service.category.category_type)
    serializer = ServiceSerializer(services, many=True)

    return Response(
        {"serializer": serializer.data, "category_names": category_names},
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_service_by_id(request, id):
    category_name = []
    service = get_object_or_404(Service, id=id)
    category_name.append(service.category.category_type)
    serializer = ServiceSerializer(service, many=True)

    serializer = ServiceSerializer(service)
    return Response(
        {"serializer": serializer.data, "category_name": category_name},
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_service(request):
    print(request.data)
    serializer = ServiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
