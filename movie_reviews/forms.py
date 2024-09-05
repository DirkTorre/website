from django import forms
import re

from .models import MovieStatus, MovieReview

class AddMovieForm(forms.Form):
     imdb_id = forms.URLField(label="IMDb URL", required=True)

     def clean_imdb_id(self):
        """
        Get the id from the url.
        """
        url = self.cleaned_data["imdb_id"]
        regex = re.compile('^tt[0-9]+')
        url = list(filter(lambda id: regex.match(id), url.split('/')))[0]
        return url


class MovieStatusForm(forms.ModelForm):
    class Meta:
        model = MovieStatus
        exclude = ['tconst']


class MovieReviewForm(forms.ModelForm):
    watch_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )
    notes = forms.DateField(
        required=False,
        widget=forms.Textarea()
    )
    class Meta:
        model = MovieReview
        exclude = ['tconst']
