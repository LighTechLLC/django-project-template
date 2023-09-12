AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "apps.users.backends.ModelBackend",
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
