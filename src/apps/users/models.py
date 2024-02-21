from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(_("email"))
    first_name = models.CharField(_("first name"), max_length=80)
    last_name = models.CharField(_("lastname"), max_length=80)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("email"), name="unique_lowered_email"
            )
        ]
