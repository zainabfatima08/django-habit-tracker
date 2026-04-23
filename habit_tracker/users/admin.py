from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "id",
        "username",
        "email",
        "is_staff",
        "is_active"
    )

    list_filter = ("is_staff", "username", "email")
    search_fields = ("username", "email")
    ordering = ("-id",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "dark_mode")
    list_filter = ("dark_mode",)