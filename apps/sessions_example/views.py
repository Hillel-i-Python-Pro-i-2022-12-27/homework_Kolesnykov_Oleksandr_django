from django.views.generic import TemplateView
from datetime import datetime

KEY__COUNT_OF_VISITS = "count_of_visits"
KEY__DATE_OF_VISIT_NOW = "date_of_visit_now"
KEY__DATE_OF_LAST_VISIT = "date_of_visit_last"


class SessionExampleView(TemplateView):
    template_name = "sessions_example/index.html"

    def get_context_data(self, **kwargs):
        session = self.request.session

        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[KEY__COUNT_OF_VISITS] = count_of_visits

        session_time_now = session.get(KEY__DATE_OF_VISIT_NOW, str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        session_time_last = session_time_now
        session_time_now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        session[KEY__DATE_OF_VISIT_NOW] = session_time_now
        session[KEY__DATE_OF_LAST_VISIT] = session_time_last

        context = super().get_context_data(**kwargs)
        context["count_of_visits"] = count_of_visits
        context["date_of_visit_now"] = session_time_now
        context["date_of_visit_last"] = session_time_last
        return context
