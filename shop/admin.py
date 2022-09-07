from django.contrib import admin

from shop.models import Product, Purchase


class PurchaseInline(admin.TabularInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "color", "cost", "external_id")
    search_fields = ("title", "external_id")
    inlines = [
        PurchaseInline,
    ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count")
    list_filter = ("count",)
    search_fields = ("product__title",)