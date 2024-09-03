from django.db import models
from django.urls import reverse

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
    ),
    'enjoyment': (
        (0, "0: dislike"),
        (0.5, "0.5"),
        (1, "1: mweh"),
        (1.5, "1.5"),
        (2, "2: fun"),
        (2.5, "2.5"),
        (3, "3: good / cool"),
        (3.5, "3.5"),
        (4, "4: great")
    ),
    'quality': (
        (0, "0: bad, not worth watching"),
        (0.5, "0.5"),
        (1, "1: bad, but interesting"),
        (1.5, "1.5"),
        (2, "2: good enough"),
        (2.5, "2.5"),
        (3, "3: good"),
        (3.5, "3.5"),
        (4, "4: great")
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
    enjoyment = models.SmallIntegerField(choices=CHOICES['enjoyment'], null=True)
    quality = models.SmallIntegerField(choices=CHOICES['quality'], null=True)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Watched Dates'
    
    def get_url(self):
        return 'LINK TO UPDATEVIEW'
        # return reverse('movie_reviews:review-add', kwargs={'pk': self.kwargs['pk']})