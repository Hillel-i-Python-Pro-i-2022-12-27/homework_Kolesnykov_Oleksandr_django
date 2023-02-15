from django.shortcuts import render
from apps.first_example.actions.create_accounts import create_account_for_users_from_generator


def create_users_accounts(request):
    return render(
        request=request,
        template_name="first_example/users.html",
        context={
            "users": create_account_for_users_from_generator(),
        },
    )


def create_users_accounts_amount(request, amount=5):
    return render(
        request=request,
        template_name="first_example/users.html",
        context={"users": create_account_for_users_from_generator(amount=amount), "amount": amount},
    )
