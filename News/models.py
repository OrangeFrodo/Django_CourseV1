from django.db import models

# Create your models here.

class Tweet (models.Model):
    # id = models.AutoField(primary_keys = True)
    content = models.TextField(blank=True, null=True)