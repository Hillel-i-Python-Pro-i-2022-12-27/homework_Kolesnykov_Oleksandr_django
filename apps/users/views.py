from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView


User = get_user_model()


class SignUpView(CreateView):
    success_url = reverse_lazy("login")

    class Mete:
        model = User
        fields = ("username",)
