from django.views.generic import TemplateView
from datetime import datetime

KEY__COUNT_OF_VISITS = "count_of_visits"
KEY__DATETIME_OF_LAST_VISIT = "datetime_of_last_visit"


class SessionExampleView(TemplateView):
    template_name = "sessions_example/index.html"

    def get_context_data(self, **kwargs):
        session = self.request.session

        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[KEY__COUNT_OF_VISITS] = count_of_visits

        datetime_now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        datetime_of_last_visit = session.get(KEY__DATETIME_OF_LAST_VISIT, "This is your first visit, hello !")
        session[KEY__DATETIME_OF_LAST_VISIT] = datetime_now

        context = super().get_context_data(**kwargs)
        context["count_of_visits"] = count_of_visits
        context["datetime_now"] = datetime_now
        context["datetime_of_last_visit"] = datetime_of_last_visit
        return context
