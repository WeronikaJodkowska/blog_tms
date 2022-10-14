from rest_framework import serializers

from api.profiles.serializers import UserSerializer
from shop.models import COLOR_CHOICES


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    color = serializers.ChoiceField(choices=COLOR_CHOICES)
    cost = serializers.IntegerField()


class PopularProductSerializer(ProductSerializer):
    sold = serializers.IntegerField()


class PurchaseSerializer(serializers.Serializer):
    user = UserSerializer()
    product = ProductSerializer()
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        return obj.product.cost * obj.count


class PurchaseCreateSerializer(serializers.Serializer):
    count = serializers.IntegerField()
