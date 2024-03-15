from django.db import models

# Create your models here.


class ChatMess(models.Model):
    chat = models.ForeignKey("chat.Chat", on_delete=models.CASCADE, related_name="chat")
    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="usermess"
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " - " + self.message
