from django.db import models

from services.models import Service
from users.models import CustomUser

# Create your models here.


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("cuidados", "Cuidado"),
        ("trabajo_manual", "Trabajo manual"),
        ("mascotas", "Mascotas"),
        ("otros", "Otros"),
    ]
    category_type = models.TextField(choices=CATEGORY_CHOICES)
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE, null=True)

    def str(self):
        return self.category_type + " - " + self.user.username
