from django.db import models

from users.models import CustomUser

# Create your models here.


class Chat(models.Model):
    user1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user1chat"
    )
    user2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user2chat"
    )

    def __str__(self):
        return self.user1.username + " - " + self.user2.username
