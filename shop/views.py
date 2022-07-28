from django.http import HttpResponse

from shop.models import Product


def products(request):
    if request.GET.get('color'):
        product_list = Product.objects.filter(color=request.GET.get('color'))
    else:
        product_list = Product.objects.all()
    return HttpResponse(", ".join([x.title for x in product_list]))