from django.contrib import admin
from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'department', 'phone_number', 'created_at', 'modified_at', 'is_auto_generated')
    list_filter = ('is_auto_generated', 'department')


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')
    list_filter = ('name',)
