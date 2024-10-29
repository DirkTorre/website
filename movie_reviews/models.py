from django.db import models
from django.urls import reverse

CHOICES = {
    "enjoyment": (
        (0.0, "0: dislike"),
        (0.5, "0.5"),
        (1.0, "1: mweh"),
        (1.5, "1.5"),
        (2.0, "2: fun"),
        (2.5, "2.5"),
        (3.0, "3: good / cool"),
        (3.5, "3.5"),
        (4.0, "4: great"),
    ),
    "quality": (
        (0.0, "0: bad, not worth watching"),
        (0.5, "0.5"),
        (1.0, "1: bad, but interesting"),
        (1.5, "1.5"),
        (2.0, "2: good enough"),
        (2.5, "2.5"),
        (3.0, "3: good"),
        (3.5, "3.5"),
        (4.0, "4: great"),
    ),
}


class MovieStatus(models.Model):
    # TODO: figure out if th options can be turned into a class,
    # so they are encapsulated for every field.
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
    AVAILABILITY_AVAILABLE = True
    AVAILABILITY_NOT_AVAILABLE = False
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

    def __str__(self):
        return self.tconst

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


class MovieDataFiles(models.Model):
    file_name = models.CharField(unique=True, max_length=50, null=False)
    imdb_path = models.URLField(unique=True, null=False)
    output_path = models.URLField(null=False, blank=True)
    last_successful_download = models.DateTimeField(null=True, blank=True)
    progress = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Movie Data Files"
