CELERY_BROKER_URL = config["celery"]["broker_url"]
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TIME_LIMIT = config["celery"]["task_time_limit"]
CELERY_TASK_ACKS_LATE = False
CELERY_RESULT_BACKEND = None
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": config["celery"]["visibility_timeout"],
    "polling_interval": config["celery"]["polling_interval"],
}

CELERY_BEAT_SCHEDULE = {}
CELERY_IMPORTS = [
    "services.celery_tasks.dummy",
]
