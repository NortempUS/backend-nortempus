from django.db import models

from services.models import Service
from users.models import CustomUser

# Create your models here.


class UserService(models.Model):
    user1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user1"
    )
    user2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user2"
    )
    service1 = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service1"
    )
    service2 = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service2"
    )

    def str(self):
        return self.user1.username + " - " + self.user2.username
