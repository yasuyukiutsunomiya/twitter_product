from django.contrib import admin
from .models import User, Tweet

# Register your models here.
admin.site.register(User, Tweet)

# @admin.register(User, Tweet)
# class ItemAdmin(admin.ModelAdmin):
#     pass