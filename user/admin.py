from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "created",
        "is_staff",
        "is_superuser",
    )


admin.site.register(models.User, UserAdmin)