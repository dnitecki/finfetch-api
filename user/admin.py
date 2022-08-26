from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    exclude = [
        "key"
    ]

    list_display = (
        "id",
        "email",
        "created",
        "key",
        # "api_key",
        "is_staff",
        "is_superuser",
    )


admin.site.register(models.User, UserAdmin)