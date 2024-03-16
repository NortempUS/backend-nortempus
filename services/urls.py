from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("list-services", views.list_services),
    path(
        "list-services-receiver/<int:receiver_id>", views.list_services_by_receiver_id
    ),
    path("update-service/<int:service_id>", views.update_service),
    path("list-service/<int:service_id>", views.list_service_by_id),
    path("create-service", views.create_service),
]
