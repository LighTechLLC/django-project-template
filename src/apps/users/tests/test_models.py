import pytest
from django.db import IntegrityError

from ..models import User

@pytest.mark.django_db
class TestUser:
    def test_same_email_uniqueness(self):
        email = "test@example.com"
        User.objects.create_user(email=email, password="pass")
        with pytest.raises(IntegrityError):
            User.objects.create_user(email=email, password="pass")

    def test_case_insensitive_email_uniqueness(self):
        email = "test@example.com"
        email1 = email.lower()
        email2 = email.upper()
        assert email1 != email2
        User.objects.create_user(email=email1, password="pass")
        with pytest.raises(IntegrityError):
            User.objects.create_user(email=email2, password="pass")
