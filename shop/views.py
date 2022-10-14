from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render

from shop.models import Product
from shop.services import get_sorted_product


def products(request):
    color = request.GET.get("color")
    order_by = request.GET.get("order_by")
    page_number = request.GET.get("page")
    user_id = request.user.id if request.user.is_authenticated else 0
    cache_key = f"products_view.{user_id}.{color}.{order_by}.{page_number}"

    result = cache.get(cache_key)
    if result is not None:
        return result
    # cost_out_of_stock.delay(request)

    if color:
        product_list = Product.objects.filter(color=color)
    else:
        product_list = Product.objects.all()

    order_by = request.GET.get("order_by")
    product_list = get_sorted_product(product_list, order_by)

    page_number = request.GET.get("page")
    paginator = Paginator(product_list, 15)
    paginator = paginator.get_page(page_number)

    response = render(request, "index.html", {"paginator": paginator})
    cache.set(cache_key, response, 60 * 60)

    return response
