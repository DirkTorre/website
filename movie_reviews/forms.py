from django import forms
import re

from .models import MovieStatus, CHOICES

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
    status = forms.TypedChoiceField(
            choices=CHOICES['status'],
            required=False,
            empty_value=None
        )
    prime = forms.TypedChoiceField(
            choices=CHOICES['available'],
            required=False,
            empty_value=None
        )
    netflix = forms.TypedChoiceField(
            choices=CHOICES['available'],
            required=False,
            empty_value=None
        )
    class Meta:
        model = MovieStatus
        exclude = ['tconst']

