"""
URL configuration for nortempus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework.schemas import get_schema_view

class CustomAutoSchema(AutoSchema):
    def get_links(self, path, method, base_url):
        links = super().get_links(path, method, base_url)
        if method.lower() == 'get':
            links.append({
                'name': 'create',
                'method': 'POST',
                'url': base_url + path,
                'description': 'Create a new service',
            })
        return links

schema_view = get_schema_view(
    version='1.0.0',
    public=True,
    permission_classes=(AllowAny,),
    patterns=[
        path('admin/', admin.site.urls),
        path('api/', include('nortempus.urls')),
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('docs/', schema_view, name='schema-swagger-ui'),    path("", include("users.urls")),
    path("", include("users.urls")),
    path("", include("services.urls")),
    path("", include("chat.urls")),
    path("", include("chatmess.urls")),
]
