from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("list-services/", views.list_services),
    path("create-service/",views.create_service)
]
