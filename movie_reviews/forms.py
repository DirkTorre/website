from django.forms import ModelForm
from .models import Movie, Scores


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['ttnumber', 'watched', 'priority', 'netflix', 'prime']

class ScoresForm(ModelForm):
    class Meta:
        model = Scores
        fields = ['watch_date', 'enjoyment', 'story', 'subject', 'acting', 'script', 'visual', 'action', 'comedy']