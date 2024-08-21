from django.db.models.signals import pre_save
from django.dispatch import receiver

from movie_reviews.models import WatchedStatus


@receiver(pre_save, sender=WatchedStatus)
def check_watched_status_change(sender, instance, **kwargs):
    if instance.pk:
        previous = WatchedStatus.objects.get(pk=instance.pk)
        message = 'updated:\n'
        if previous.status != instance.status:
            message += f"- status from {previous.status} to {instance.status}.\n"
        if previous.priority != instance.priority:
            message += f"- priority from {previous.priority} to {instance.priority}."
        return message