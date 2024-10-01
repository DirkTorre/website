from django import forms
from django.core.exceptions import ValidationError
import re

from .models import MovieReview


class AddMovieForm(forms.Form):
    imdb_id = forms.URLField(label="IMDb URL", required=True)

    def clean_imdb_id(self):
        """
        Get the id from the url.
        """
        url = self.cleaned_data["imdb_id"]
        if "www.imdb.com/" not in url:
            raise ValidationError("URL does not originate from IMDb.com")
        if not re.compile("/tt[0-9]+").search(url):
            raise ValidationError("tconst not found")
        regex = re.compile("^tt[0-9]+")
        tconst = list(filter(lambda id: regex.match(id), url.split("/")))[0]
        return tconst


class MovieReviewForm(forms.ModelForm):
    watch_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )
    notes = forms.CharField(required=False, widget=forms.Textarea(), empty_value=None)

    class Meta:
        model = MovieReview
        exclude = ["tconst"]
