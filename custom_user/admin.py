from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "display_name",
    )
    list_filter = (
        "username",
        "display_name",
    )
    fieldsets = ((None, {"fields": ("username", "display_name",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
