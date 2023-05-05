from celery import shared_task


@shared_task(name="dummy_task")
def dummy_task():
    pass
