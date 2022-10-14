from django_filters import FilterSet, NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.shop.serializers import (
    PopularProductSerializer,
    ProductSerializer,
    PurchaseCreateSerializer,
    PurchaseSerializer,
)
from shop.models import Product, Purchase
from shop.services import get_popular_products


class ProductFilter(FilterSet):

    min_cost = NumberFilter(field_name="cost", lookup_expr="gte")
    max_cost = NumberFilter(field_name="cost", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["title"]


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_class = ProductFilter
    search_fields = ["title", "color"]
    ordering_fields = ["title", "cost"]


class PurchaseList(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            # raise NotAuthenticated
            return Purchase.objects.none()
        return Purchase.objects.filter(user=self.request.user)


class ProductPurchaseView(generics.CreateAPIView):
    serializer_class = PurchaseCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            product = Product.objects.get(id=kwargs.get("product_id"))
            Purchase.objects.create(
                user=request.user,
                product=product,
                count=serializer.validated_data["count"],
            )
            return Response(status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PopularProductList(generics.ListAPIView):
    serializer_class = PopularProductSerializer
    queryset = get_popular_products()
