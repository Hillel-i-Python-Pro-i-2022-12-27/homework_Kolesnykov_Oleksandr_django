# from django.contrib.auth.decorators import login_required
from django.urls import path
import apps.first_example.views as views

app_name = "first_example"

urlpatterns = [
    path("greetings", views.greetings_with_name_and_age, name="greetings_default"),
    path("users_accounts", views.create_users_accounts, name="users_accounts"),
    path("users_accounts_amount/<int:amount>", views.create_users_accounts_amount, name="users_accounts_amount"),
]
