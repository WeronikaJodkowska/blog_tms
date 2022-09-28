import requests

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

COLOR_CHOICES = (('red', 'Red color'), ('green', 'Green color'), ('white', 'White color'))
STATUS_CHOICES = (('IN_STOCK', ' In Stock'), ('BACK_ORDER', 'Back order'),
                  ('DISCONTINUED', 'Discontinued'), ('OUT_OF_STOCK', 'Out of Stock'))


class Product(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=COLOR_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    cost = models.IntegerField()
    external_id = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Product: {self.title}"


@receiver(post_save, sender=Product, dispatch_uid="send_message")
def update_stock(sender, instance, **kwargs):
    message = f"Product {instance.title} is updated"
    requests.get(f"http://127.0.0.1:5000/?message={message}")


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()

    def __str__(self):
        return f"Bought {self.product.title} by: {self.user}. \t"
