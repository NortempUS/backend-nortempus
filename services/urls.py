from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("list-services", views.list_services),
    path("list-services-receiver/<int:id>", views.list_services_by_receiver_id),
    path("list-service/<int:id>", views.list_service_by_id),
    path("create-service", views.create_service),
]
