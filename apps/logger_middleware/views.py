from django.shortcuts import render
from .models import RequestsLogger


def requests_menu(request):
    return render(request=request, template_name="logger_middleware/requests_menu.html")


def list_of_requests(request):
    context = {"object_list": RequestsLogger.objects.all()}

    return render(
        request=request,
        template_name="logger_middleware/list_of_logs.html",
        context=context,
    )


def user_list_of_requests(request):
    context = {
        "object_list": RequestsLogger.objects.filter(user=request.user),
        "count_of_visits": RequestsLogger.objects.filter(user=request.user).count(),
    }
    return render(
        request=request,
        template_name="logger_middleware/user_list_of_logs.html",
        context=context,
    )


def session_list_of_requests(request):
    session_key = request.session.session_key

    context = {
        "object_list": RequestsLogger.objects.filter(session_key=session_key),
        "count_of_visits": RequestsLogger.objects.filter(session_key=session_key).count(),
    }
    return render(
        request=request,
        template_name="logger_middleware/session_list_of_logs.html",
        context=context,
    )
