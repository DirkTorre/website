from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class WatchedStatus(models.Model):
    # database fields
    tconst = models.CharField(max_length=12, primary_key=True, null=False)
    status = models.BooleanField(default=False)
    priority = models.BooleanField(default=False, null=True)

    # class variable (i think)
    _old_status = None
    _old_priority = None

    class Meta:
        verbose_name_plural = 'Watched Status'
    
    @classmethod
    def from_db(cls, db, field_names, values):
        """
        Override class method.
        """
        instance = super().from_db(db, field_names, values)
        # Cache old values
        instance._old_status = instance.status
        instance._old_priority = instance.priority
        
        return instance
    
    def changed_status(self):
        return self._old_status != self.status

    def changed_priority(self):
        return self._old_status != self.status


class WatchedDates(models.Model):
    tconst = models.ForeignKey(to=WatchedStatus, null=False, on_delete=models.DO_NOTHING)
    watch_date = models.DateField(null=True)
    enjoyment = models.SmallIntegerField()
    quality = models.SmallIntegerField(null=True)


    class Meta:
        verbose_name_plural = 'Watched Dates'

class Availability(models.Model):
    tconst = models.ForeignKey(to=WatchedStatus, null=False, on_delete=models.DO_NOTHING)
    netflix = models.BooleanField(null=True)
    prime = models.BooleanField(null=True)

    class Meta:
        verbose_name_plural = 'Availability'