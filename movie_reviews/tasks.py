from celery import shared_task
from time import sleep


@shared_task()
def download_files(files, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
