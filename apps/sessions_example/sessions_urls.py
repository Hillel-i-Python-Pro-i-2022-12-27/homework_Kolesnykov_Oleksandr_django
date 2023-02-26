from django.urls import path
from apps.sessions_example import views

app_name = "sessions_example"

urlpatterns = [
    path("", views.SessionExampleView.as_view(), name="index"),
]
