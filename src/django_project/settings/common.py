DEBUG = config["base"]["debug"]

SECRET_KEY = config["base"]["secret_key"]

ALLOWED_HOSTS = config["base"]["allowed_hosts"]

CSRF_TRUSTED_ORIGINS = config["base"]["csrf_trusted_origins"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ROOT_URLCONF = "django_project.urls"

WSGI_APPLICATION = "django_project.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FORCE_SCRIPT_NAME = config["base"]["script_name"]

if FORCE_SCRIPT_NAME:
    SESSION_COOKIE_PATH = f"{FORCE_SCRIPT_NAME}/"

SILENCED_SYSTEM_CHECKS = ["auth.E003"]
