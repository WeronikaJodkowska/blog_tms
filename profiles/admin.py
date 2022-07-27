from django.contrib import admin

from profiles.models import Address


@admin.register(Address)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "street")
    fields = ("user", "zipcode", "city", "street", "building", "room")
    search_fields = ("user", "city", "street")
