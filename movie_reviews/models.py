from django.db import models
from django.urls import reverse

CHOICES = {
    "enjoyment": (
        (0, "0: dislike"),
        (0.5, "0.5"),
        (1, "1: mweh"),
        (1.5, "1.5"),
        (2, "2: fun"),
        (2.5, "2.5"),
        (3, "3: good / cool"),
        (3.5, "3.5"),
        (4, "4: great"),
    ),
    "quality": (
        (0, "0: bad, not worth watching"),
        (0.5, "0.5"),
        (1, "1: bad, but interesting"),
        (1.5, "1.5"),
        (2, "2: good enough"),
        (2.5, "2.5"),
        (3, "3: good"),
        (3.5, "3.5"),
        (4, "4: great"),
    ),
}


class MovieStatus(models.Model):
    STATUS_UNKNOWN = None
    STATUS_WATCHED = True
    STATUS_NOT_WATCHED = False
    STATUS_CHOICES = (
        (STATUS_UNKNOWN, "unknown"),
        (STATUS_WATCHED, "watched"),
        (STATUS_NOT_WATCHED, "not watched"),
    )
    PRIORITY_YES = True
    PRIORITY_NO = False
    PRIORITY_CHOICES = (
        (PRIORITY_YES, "yes"),
        (PRIORITY_NO, "no"),
    )
    AVAILABILITY_UNKNOWN = None
    AVAILABILITY_AVAILABLE = None
    AVAILABILITY_NOT_AVAILABLE = None
    AVAILABILITY_CHOICES = (
        (AVAILABILITY_UNKNOWN, "unknown"),
        (AVAILABILITY_AVAILABLE, "available"),
        (AVAILABILITY_NOT_AVAILABLE, "not available"),
    )
    tconst = models.CharField(max_length=12, unique=True, null=False)
    status = models.BooleanField(
        default=False, null=True, blank=True, choices=STATUS_CHOICES
    )
    priority = models.BooleanField(
        default=False, null=False, blank=False, choices=PRIORITY_CHOICES
    )
    netflix = models.BooleanField(
        default=None, null=True, blank=True, choices=AVAILABILITY_CHOICES
    )
    prime = models.BooleanField(
        default=None, null=True, blank=True, choices=AVAILABILITY_CHOICES
    )

    class Meta:
        verbose_name_plural = "Movie Status"


class MovieReview(models.Model):
    tconst = models.ForeignKey(to=MovieStatus, null=False, on_delete=models.DO_NOTHING)
    watch_date = models.DateField(null=True, blank=True)
    enjoyment = models.DecimalField(
        choices=CHOICES["enjoyment"],
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
    )
    quality = models.DecimalField(
        choices=CHOICES["quality"],
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
    )
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Movie Reviews"
