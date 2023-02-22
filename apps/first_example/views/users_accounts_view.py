from django.shortcuts import render
from apps.first_example.actions.create_users import create_generator_of_humans


def create_users_accounts(request):
    return render(
        request=request,
        template_name="first_example/users.html",
        context={
            "users": create_generator_of_humans(),
        },
    )


def create_users_accounts_amount(request, amount=5):
    return render(
        request=request,
        template_name="first_example/users.html",
        context={"users": create_generator_of_humans(amount=amount), "amount": amount},
    )
