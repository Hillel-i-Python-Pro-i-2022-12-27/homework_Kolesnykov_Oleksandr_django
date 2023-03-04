from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginFormView.as_view(), name="login"),
    path("signup/", views.RegisterFormView.as_view(), name="signup"),
    path("update_profile/<int:pk>", views.UserUpdateView.as_view(), name="update_profile"),
    path("profile/<int:pk>", views.UserDetailView.as_view(), name="profile"),
]
