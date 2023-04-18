from .models import RequestsLogger


class RequestsLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user_id = request.user.id
        path = request.path
        session_key = request.session.session_key
        request_logger = RequestsLogger.objects

        if request_logger.filter(
            user_id=user_id,
            path=path,
            session_key=session_key,
        ).exists():
            request_log = request_logger.get(
                user_id=user_id,
                path=path,
                session_key=session_key,
            )
            request_log.update_log()

        else:
            request_logger.create(
                user_id=user_id,
                path=path,
                session_key=session_key,
            )

        return response
