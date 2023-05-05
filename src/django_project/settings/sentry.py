import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if config["sentry"]["dsn"]:
    sentry_sdk.init(
        dsn=config["sentry"]["dsn"],
        integrations=[DjangoIntegration()],
        auto_session_tracking=False,
        traces_sample_rate=0.01,
        environment=config["sentry"]["environment"],
    )
