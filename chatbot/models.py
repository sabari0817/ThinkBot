from django.db import models

class ChatSession(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    history = models.JSONField(default=list)

    def __str__(self):
        return self.user_id
