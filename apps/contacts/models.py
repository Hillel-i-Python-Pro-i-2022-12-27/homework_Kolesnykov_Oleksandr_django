from django.db import models


class Contact(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.user_name} - phone number: {self.phone_number}"

    __repr__ = __str__
