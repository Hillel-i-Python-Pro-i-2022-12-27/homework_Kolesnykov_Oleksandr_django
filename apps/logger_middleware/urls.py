from django.urls import path
from apps.logger_middleware.views import (
    list_of_requests,
    user_list_of_requests,
    session_list_of_requests,
    requests_menu,
)


app_name = "requests"

urlpatterns = [
    path("requests_menu", requests_menu, name="requests_menu"),
    path("requests_list/all", list_of_requests, name="list_of_requests"),
    path("requests_list/user", user_list_of_requests, name="user_list_of_requests"),
    path("requests_list/session", session_list_of_requests, name="session_list_of_requests"),
]
