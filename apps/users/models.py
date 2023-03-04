from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    photo = models.ImageField(
        max_length=255,
        upload_to="users/user/profile_photo",
        blank=True,
        null=True,
    )
