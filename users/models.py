from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    GENDER_CHOICES = [
        ("hombre", "Hombre"),
        ("mujer", "mujer"),
        ("otro", "Otro"),
        ("prefiero no decir", "Prefiero no decir"),
    ]
    gender = models.TextField(choices=GENDER_CHOICES, null=True, blank=True)
    total_points = models.PositiveIntegerField(default=0)
    number_of_services = models.PositiveIntegerField(default=0)
    PLAN_CHOICES = [("basico", "Básico"), ("premium", "Premium")]
    plan = models.TextField(choices=PLAN_CHOICES, default="basico")

    def __str__(self):
        return self.username
