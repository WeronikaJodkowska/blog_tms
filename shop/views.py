from django.db.models import Sum, Max, Min, F
from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Product, Purchase
from shop.services import get_sorted_product


def products(request):
    if request.GET.get("color"):
        product_list = Product.objects.filter(color=request.GET.get("color"))
    else:
        product_list = Product.objects.all()
    order_by = request.GET.get("order_by")

    product_list = get_sorted_product(product_list, order_by)
    return render(request, "index.html", {"product_list": product_list})

# 20 homework. 3. Добавить сортировку товаров через GET параметр по цене,
# продажам (по общей стоимости продаж) и популярности (по количеству проданных).
def get_products_by_price(request):
    sort_by = request.GET.get("sort", "l2h")
    if sort_by == "l2h":
        product_list = Product.objects.order_by("cost")
    elif sort_by == "h2l":
        product_list = Product.objects.order_by("-cost")
    else:
        product_list = Product.objects.all()
    return HttpResponse(", ".join([x.title for x in product_list]))


def get_products_by_purchases(request):
    sort_by = request.GET.get("sort", "l2h")
    if sort_by == "l2h":
        result = Purchase.objects.values('product__title').annotate(purchase_count=Sum(F("count") * F("product__cost")))\
            .order_by("purchase_count")
    elif sort_by == "h2l":
        result = Purchase.objects.values('product__title').annotate(purchase_count=Sum(F("count") * F("product__cost")))\
            .order_by("-purchase_count")
    else:
        result = Purchase.objects.values('product__title').annotate(purchase_count=Sum(F("count") * F("product__cost")))
    return HttpResponse(result)


def get_popular_product(request):
    sort_by = request.GET.get("sort", "max")
    if sort_by == "max":
        result = Purchase.objects.aggregate(max_purchase=Max("count"))
        product = Product.objects.filter(purchases__count__exact=result['max_purchase'])
    elif sort_by == "min":
        result = Purchase.objects.aggregate(max_purchase=Min("count"))
        product = Product.objects.filter(purchases__count__exact=result['max_purchase'])

    else:
        product = Product.objects.all()
    return HttpResponse(product)
