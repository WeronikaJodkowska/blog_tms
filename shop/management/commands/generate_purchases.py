from random import randint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from shop.models import Product, Purchase


class Command(BaseCommand):
    help = "Generate purchases"

    def handle(self, *args, **options):
        i = 0
        while i < 100:
            user = User.objects.order_by("?").last()
            product = Product.objects.order_by("?").last()
            count = randint(1, 5)
            Purchase.objects.create(user=user, product=product, count=count)
            i += 1
