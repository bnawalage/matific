from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from demo.cbv_demo.models import User

admin.site.register(User, UserAdmin)


# Register your models here.
def save_model(self, request, obj, form, change):
    obj.created_by = request.user
    super().save_model(request, obj, form, change)
