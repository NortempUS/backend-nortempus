from django.db import models

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def str(self):
        return self.category_type + " - " + self.user.username
