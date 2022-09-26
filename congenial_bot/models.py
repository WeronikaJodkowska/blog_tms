from django.db import models


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    sender = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
