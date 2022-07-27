from django.conf import settings
from django.db import models


# 1. Добавить модель Address со связью One-To-Many к модели User.

class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
        blank=True,
        null=True
    )
    zipcode = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    building = models.CharField(max_length=20, blank=True, null=True)
    room = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Address of {self.user}"
