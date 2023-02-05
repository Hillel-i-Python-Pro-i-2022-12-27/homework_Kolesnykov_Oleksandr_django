from django.shortcuts import render


def greetings_with_name_and_age(request, name="Oleksandr Kolesnykov", age=25):
    return render(
        request=request,
        template_name="first_example/greetings.html",
        context={
            "name": name,
            "age": age,
        },
    )
