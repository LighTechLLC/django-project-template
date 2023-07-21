import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if SENTRY_DSN := config["sentry"]["dsn"]:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        auto_session_tracking=False,
        traces_sample_rate=0.01,
        environment=ENVIRONMENT,
    )
