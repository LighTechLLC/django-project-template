import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import ignore_logger

if SENTRY_DSN := config["sentry"]["dsn"]:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        auto_session_tracking=config["sentry"]["auto_session_tracking"],
        traces_sample_rate=0.01,
        environment=ENVIRONMENT,
    )
    ignore_logger("django.security.DisallowedHost")
