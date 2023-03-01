from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, DetailView

from apps.users.forms import RegisterUserForm


User = get_user_model()


class RegisterFormView(FormView):
    form_class = RegisterUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("root:home_page")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("root:home_page")


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "photo",
    )

    success_url = reverse_lazy("root:home_page")
