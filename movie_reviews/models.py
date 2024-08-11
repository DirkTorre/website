from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class WatchedStatus(models.Model):
    tconst = models.CharField(max_length=12, primary_key=True, null=False)
    status = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Watched Status'


class WatchedDates(models.Model):
    tconst = models.ForeignKey(to=WatchedStatus, null=False, on_delete=models.DO_NOTHING)
    watch_date = models.DateField(null=True)
    enjoyment = models.SmallIntegerField()
    quality = models.SmallIntegerField(null=True) # TODO: new field


    class Meta:
        verbose_name_plural = 'Watched Dates'

class Availability(models.Model):
    tconst = models.ForeignKey(to=WatchedStatus, null=False, on_delete=models.DO_NOTHING)
    netflix = models.BooleanField(null=True)
    prime = models.BooleanField(null=True)

    class Meta:
        verbose_name_plural = 'Availability'