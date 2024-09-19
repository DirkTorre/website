import django_filters
from django import forms
from .models import MovieStatus


class MovieStatusFilter(django_filters.FilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=MovieStatus.STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    priority = django_filters.MultipleChoiceFilter(
        choices=MovieStatus.PRIORITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    netflix = django_filters.MultipleChoiceFilter(
        choices=MovieStatus.AVAILABILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    prime = django_filters.MultipleChoiceFilter(
        choices=MovieStatus.AVAILABILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = MovieStatus
        fields = {
            "tconst": ["icontains"],
            "status": ["exact"],
            "priority": ["exact"],
            "netflix": ["exact"],
            "prime": ["exact"],
        }
