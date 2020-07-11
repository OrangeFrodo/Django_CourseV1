import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class Tweet (models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_keys = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 299)
        }