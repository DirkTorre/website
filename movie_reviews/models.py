from django.db import models

CHOICES = {
    'status': (
        (None, "unknown"),
        (True, "watched"),
        (False, "not watched")
    ),
    'priority': (
        (True, "yes"),
        (False, "no")
    ),
    'available': (
        (None, "unknown"),
        (True, "available"),
        (False, "not available")
    )
}

class MovieStatus(models.Model):
    tconst = models.CharField(max_length=12, unique=True, null=False)
    status = models.BooleanField(default=False, null=True, choices=CHOICES['status'])
    priority = models.BooleanField(default=False, null=False, choices=CHOICES['priority'])
    netflix = models.BooleanField(default=None, null=True, choices=CHOICES['available'])
    prime = models.BooleanField(default=None, null=True, choices=CHOICES['available'])

    class Meta:
        verbose_name_plural = 'Movie Status'


class WatchedDates(models.Model):
    tconst = models.ForeignKey(to=MovieStatus, null=False, on_delete=models.DO_NOTHING)
    watch_date = models.DateField(null=True)
    enjoyment = models.SmallIntegerField()
    quality = models.SmallIntegerField(null=True)


    class Meta:
        verbose_name_plural = 'Watched Dates'