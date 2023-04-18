from django.contrib import admin
from .models import RequestsLogger


@admin.register(RequestsLogger)
class RequestsLoggerAdmin(admin.ModelAdmin):
    list_display = ["user", "path", "session_key", "counter_of_visits", "last_visit"]
    list_filter = ["user"]
    search_fields = ["path"]
