from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from category.models import Category
from users.models import CustomUser

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100)
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="receiver"
    )
    provider = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="provider"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    status = models.BooleanField()
    valoration = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def str(self):
        return self.username
