from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Contact(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='contacts',
        default=None,
        null=True,
        blank=False,
    )

    def __str__(self):
        return f"Name: {self.user_name} - phone number: {self.phone_number}"

    __repr__ = __str__
