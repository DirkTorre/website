from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def create_decimal_field():
    return models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)]
    )


class Movie(models.Model):
    ttnumber = models.CharField(max_length=255, primary_key=True, null=False)
    watched = models.BooleanField(null=True)
    priority = models.BooleanField(default=False)
    netflix = models.BooleanField(null=True)
    prime = models.BooleanField(null=True)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.ttnumber) + "\t" + str(self.watched) + "\t" + str(self.priority)


class Scores(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_date = models.DateField()
    enjoyment = create_decimal_field()
    story = create_decimal_field()
    subject = create_decimal_field()
    acting = create_decimal_field()
    script = create_decimal_field()
    visual = create_decimal_field()
    action = create_decimal_field()
    comedy = create_decimal_field()
    
    def __str__(self):
        return str(self.watch_date) + "\t" + str(self.enjoyment)