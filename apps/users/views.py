from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView

#
#
User = get_user_model()
#
#
# class SignUpView(CreateView):
#     success_url = reverse_lazy("login")
#
#     class Meta:
#         model = User
#         fields = (
#             "username",
#             "email",
#             'age',
#             'sex'
#         )


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
