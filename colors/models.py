from django.contrib.auth.models import User
from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True, db_index=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
