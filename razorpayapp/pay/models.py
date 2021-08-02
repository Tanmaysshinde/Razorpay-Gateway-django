from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Forms(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    amount = models.FloatField()
