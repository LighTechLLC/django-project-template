import tomllib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# toml config file set up
CONFIG_FILE = BASE_DIR / "config.toml"

if not CONFIG_FILE.exists():
    CONFIG_FILE = BASE_DIR / "default_config.toml"

with open(CONFIG_FILE, "rb") as f:
    config = tomllib.load(f)

SECRET_KEY = config["base"]["secret_key"]
DEBUG = config["base"]["debug"]

# env name: local / dev / stage / prod
ENVIRONMENT_LOCAL = "local"
ENVIRONMENT_STAGE = "stage"
ENVIRONMENT_DEV = "dev"
ENVIRONMENT_PROD = "production"
SUPPORTED_ENVIRONMENTS = [
    ENVIRONMENT_LOCAL,
    ENVIRONMENT_STAGE,
    ENVIRONMENT_DEV,
    ENVIRONMENT_PROD,
]
ENVIRONMENT = config["base"]["environment"]

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
