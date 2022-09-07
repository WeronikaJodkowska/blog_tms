from api.shop.serializers import PurchaseSerializer, ProductSerializer
from shop.models import Purchase, Product
from rest_framework import generics
from rest_framework import filters as rest_filters
from django_filters import FilterSet, NumberFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductFilter(FilterSet):

    min_cost = NumberFilter(field_name="cost", lookup_expr="gte")
    max_cost = NumberFilter(field_name="cost", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["title"]


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [rest_filters.SearchFilter, rest_filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ["title", "color"]
    ordering_fields = ["title", "cost"]


class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            # raise NotAuthenticated
            return Purchase.objects.none()
        return Purchase.objects.filter(user=self.request.user)