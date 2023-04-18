from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class RequestsLogger(models.Model):
    path = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    session_key = models.CharField(max_length=255, null=True)
    counter_of_visits = models.PositiveIntegerField(default=1)
    last_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} | {self.path} | {self.session_key}"

    def update_log(self):
        self.counter_of_visits += 1
        self.last_visit = models.DateTimeField(auto_now=True)
        self.save()
