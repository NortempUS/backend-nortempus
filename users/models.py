from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField()
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    GENDER_CHOICES = [
        ("hombre", "Hombre"),
        ("mujer", "mujer"),
        ("otro", "Otro"),
        ("prefiero no decir", "Prefiero no decir"),
    ]
    gender = models.TextField(choices=GENDER_CHOICES)
    total_points = models.PositiveIntegerField(default=0)
    number_of_services = models.PositiveIntegerField(default=0)
    PLAN_CHOICES = [("basico", "Básico"), ("premium", "Premium")]
    plan = models.TextField(choices=PLAN_CHOICES, default="basico")

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="customuser_permissions",
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="customuser_groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )

    def __str__(self):
        return self.username
