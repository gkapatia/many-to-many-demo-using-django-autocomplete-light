from django.contrib.auth.models import User
from django.db import models

from colors.models import Color


class Car(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True, db_index=True)
    available_colors = models.ManyToManyField(Color, blank=True, through='CarAvailableColorMapping')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarAvailableColorMapping(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
