from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView
from django.views.generic.edit import ModelFormMixin

from .models import MovieStatus
from .forms import AddMovieForm, MovieStatusForm

class HomePageView(TemplateView):
    template_name = 'movie_reviews/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Welcome to the Movie Page motherfucker!'
        return context


class AddMovieView(FormView):
    template_name = "movie_reviews/movie_add.html"
    form_class = AddMovieForm
    success_url = "/movies/"

    def form_valid(self, form):
        tconst = form.cleaned_data["imdb_id"]

        movie_status, created = MovieStatus.objects.get_or_create(
            tconst = tconst,
            defaults= {
                'status': None,
                'priority': False,
                'netflix': None,
                'prime': None,
            }
        )
        self.id = movie_status.id
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('movie_reviews:movie-detail', kwargs={'pk': self.id})


class MovieDetailView(DetailView, ModelFormMixin):
    model = MovieStatus
    form_class = MovieStatusForm
    template_name = "movie_reviews/movie_details.html"
    context_object_name = 'movie_status'

    def get_success_url(self):
        return self.request.path

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_status_object'] = self.get_object()
        context['movie_status_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

