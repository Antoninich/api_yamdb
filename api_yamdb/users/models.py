from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .enums import Roles


class UserProfile(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    role = models.CharField(
        choices=Roles.choices(),
        default='user',
        max_length=50
    )
    bio = models.TextField()

    def __str__(self):
        return self.username
