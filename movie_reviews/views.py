from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView


from .models import Movie, Scores
from .forms import MovieForm, ScoresForm


# modelformset: https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
# advanced modelforms: https://www.squash.io/advance-django-forms-dynamic-generation-processing-and-custom-widgets/
# extending forms: https://www.squash.io/advance-django-forms-dynamic-generation-processing-and-custom-widgets/
# ik denk dat hier het antwoord staat >>>>>>>>>: https://stackoverflow.com/questions/50487334/django-modelform-inheritance-and-meta-inheritance


class MovieCreateView(CreateView):
    """
    works: http://127.0.0.1:8000/movie/movie/add/
    """
    model = Movie
    fields = ('ttnumber','watched','priority','netflix','prime')


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ('ttnumber','watched','priority','netflix','prime')


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie-add')


class MovieDetailView(DetailView):
    """
    This one works: http://127.0.0.1:8000/movie/movie/tt21469794/
    """
    model = Movie
    fields = ('ttnumber','watched','priority','netflix','prime')


class MovieListView(ListView):
    """
    works: http://127.0.0.1:8000/movie/movie/list/
    """
    model = Movie

# from .forms import ScoresForm, MovieForm

# class MovieCreateView(View):
#     template_name = 'movie_reviews/create.html'

#     def get(self, request):
#         movie_form = MovieForm()
#         return render(request, self.template_name, {
#             'movie_form': movie_form,
#         })

#     def post(self, request):
#         movie_form = MovieForm(request.POST)
#         if movie_form.is_valid():
#             scores = scores_form.save()
#             movie = movie_form.save(commit=False)
#             movie.scores = scores
#             movie.save()
#             scores_form = ScoresForm()
#             movie_form = MovieForm()
#         return render(request, self.template_name, {
#             'scores_form': scores_form,
#             'movie_form': movie_form,
#         })