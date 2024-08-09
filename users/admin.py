from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "login",
        "phone_number",
        "birth_date",
        "date_created",
        "date_modified",
    )
    search_fields = ("login", "phone_number")
