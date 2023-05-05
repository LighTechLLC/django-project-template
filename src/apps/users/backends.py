from django.contrib.auth.backends import ModelBackend as DjangoModelBackend

from apps.users.models import User


class ModelBackend(DjangoModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return

        filter_key = f"{User.USERNAME_FIELD}__iexact"
        try:
            user = User._default_manager.get(**{filter_key: username})
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(
                user
            ):
                return user
