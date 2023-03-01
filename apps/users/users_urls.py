from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterFormView.as_view(), name="signup"),
    path("user_update/<int:pk>", views.UserUpdateView.as_view(), name="user_update"),
    path("user_detail/<int:pk>", views.UserDetailView.as_view(), name="user_detail"),
]
