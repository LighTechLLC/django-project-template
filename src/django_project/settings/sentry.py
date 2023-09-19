import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import ignore_logger

if SENTRY_DSN := config["sentry"]["dsn"]:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration(), CeleryIntegration()],
        auto_session_tracking=config["sentry"]["auto_session_tracking"],
        traces_sample_rate=config["sentry"]["traces_sample_rate"],
        environment=ENVIRONMENT,
    )
    ignore_logger("django.security.DisallowedHost")
