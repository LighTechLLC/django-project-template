import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIAbstractModel(models.Model):
    """
    Shortcut for setting up UUID as a primary key field instead of using
    default django behaviour- BigInteger.
    """

    id = models.UUIDField(
        _("ID"), editable=False, default=uuid.uuid4, primary_key=True
    )

    class Meta:
        abstract = True


class TimeStampedAbstractModel(models.Model):
    """Shortcut for adding up creation and update timestamps."""

    created_timestamp = models.DateTimeField(
        _("created at"), auto_now_add=True, editable=False
    )
    updated_timestamp = models.DateTimeField(
        _("updated at"), auto_now=True, editable=False
    )

    class Meta:
        abstract = True
