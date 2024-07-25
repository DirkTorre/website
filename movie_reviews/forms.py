from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import WatchedStatus
import re


# class MovieForm(ModelForm):
#     class Meta:
#         model = Movie
#         fields = ['ttnumber', 'watched', 'priority', 'netflix', 'prime']

# class ScoresForm(ModelForm):
#     class Meta:
#         model = Scores
#         fields = ['watch_date', 'enjoyment', 'story', 'subject', 'acting', 'script', 'visual', 'action', 'comedy']


RADIOSELECT_CHOICES = [
        (None, "Unknown"),
        (True, "Yes"),
        (False, "No"),
        ]

class AddWatchedMovieForm(forms.Form):
    ENJOYMENT_CHOICES = [
        (None, "No review"),
        (1, "1/5\tBAD!"),
        (2, "1.5/5"),
        (3, "2/5\tmweh..."),
        (4, "2.5/5"),
        (5, "3/5\tfun"),
        (6, "3.5/5"),
        (7, "4/5\tgood/cool"),
        (8, "4.5/5"),
        (9, "5/5\tGREAT!")
        ]
    
    imdb_id = forms.URLField(label="IMDb URL", required=True)
    date = forms.DateField(label="Watch date", required=False, widget=forms.NumberInput(attrs={'type': 'date'}))
    enjoyment = forms.ChoiceField(choices = ENJOYMENT_CHOICES, required=False)
    netflix = forms.NullBooleanField(label="Available on Netflix?", widget=forms.RadioSelect(choices=RADIOSELECT_CHOICES))
    prime = forms.BooleanField(label="Available on Prime?", required=False, widget=forms.RadioSelect(choices=RADIOSELECT_CHOICES))

    def clean_imdb_id(self):
        """
        Get the id from the url.
        """
        url = self.cleaned_data["imdb_id"]
        regex = re.compile('^tt[0-9]+')
        url = list(filter(lambda id: regex.match(id), url.split('/')))[0]

        return url


class AddUnwatchedMovieForm(forms.Form):
    imdb_url = forms.URLField(label="Movie URL", required=True)
    priority = forms.BooleanField(label="Priority?")
    netflix = forms.NullBooleanField(label="Available on Netflix?", widget=forms.RadioSelect(choices=RADIOSELECT_CHOICES))
    prime = forms.BooleanField(label="Available on Prime?", required=False, widget=forms.RadioSelect(choices=RADIOSELECT_CHOICES))

    # https://micropyramid.com/blog/understanding-djangos-model-formsets-in-detail-and-their-advanced-usage

    # https://docs.djangoproject.com/en/5.0/topics/forms/formsets/

# AddUnwatchedMoviesFormSet = modelformset_factory(WatchedStatus, form=AddUnwatchedMovie)