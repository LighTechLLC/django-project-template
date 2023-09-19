AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
