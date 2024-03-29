from django.contrib import admin

from congenial_bot.models import Message


@admin.register(Message)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "text", "message", "created_at")
