from django.views.generic.edit import FormView, CreateView
from django.views.generic import TemplateView

from .forms import AddWatchedMovieForm, AddUnwatchedMovieForm

from .models import WatchedStatus, WatchedDates, Availability


class AddWatchedMovieView(FormView):
    template_name = "movie_reviews/add_watched_movie.html"
    form_class = AddWatchedMovieForm
    success_url = "/movies/"

    def form_valid(self, form):
        # is dit de goede plek om dit neer te zetten

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        id = form.cleaned_data["imdb_id"]
        date = form.cleaned_data["date"]
        enjoyment = form.cleaned_data["enjoyment"]
        netflix = form.cleaned_data["netflix"]
        prime = form.cleaned_data["prime"]

        # edit or add watched status
        watched_status_obj, created = WatchedStatus.objects.update_or_create(
           tconst = id,
           status = True
        )
        watched_status_obj.save()

        # add watched date
        # might add a duplicate
        if date != None:
            obj = WatchedDates.objects.create(
                tconst = watched_status_obj,
                watch_date = date,
                enjoyment = int(enjoyment)
            )
            obj.save()

        # add or update netflix status
        if netflix != None:
            # edit or add watched status
            obj, created = Availability.objects.update_or_create(
                tconst = watched_status_obj,
                netflix = netflix
            )
            obj.save()
        
        # add or update prime status
        if prime != None:
            # edit or add watched status
            obj, created = Availability.objects.update_or_create(
                tconst = watched_status_obj,
                prime = netflix
            )
            obj.save()


        return super(AddWatchedMovieView, self).form_valid(form)


class AddUnwatchedMovieView(FormView):
    template_name = "movie_reviews/add_unwatched_movie.html"
    form_class = AddUnwatchedMovieForm
    success_url = "/movies/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


# class AddUnwatchedMovieView(TemplateView):
#     template_name = "movie_reviews/add_unwatched_movie.html"
#     success_url = "/movies/"

#     def get(self):
#         formset = AddUnwatchedMoviesFormSet()
#         return self.render_to_response({"formset": formset})
    
#     def post(self):
#         formset = AddUnwatchedMoviesFormSet(data = self.request.POST)

#         if formset.is_valid():
#             formset.save()
        
#         return self.render_to_response({"formset": formset})

# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.http import HttpResponse
# from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView


# from .models import Movie, Scores
# from .forms import MovieForm, ScoresForm


# # modelformset: https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
# # advanced modelforms: https://www.squash.io/advance-django-forms-dynamic-generation-processing-and-custom-widgets/
# # extending forms: https://www.squash.io/advance-django-forms-dynamic-generation-processing-and-custom-widgets/
# # ik denk dat hier het antwoord staat >>>>>>>>>: https://stackoverflow.com/questions/50487334/django-modelform-inheritance-and-meta-inheritance


# class MovieCreateView(CreateView):
#     """
#     works: http://127.0.0.1:8000/movie/movie/add/
#     """
#     model = Movie
#     fields = ('ttnumber','watched','priority','netflix','prime')


# class MovieUpdateView(UpdateView):
#     model = Movie
#     fields = ('ttnumber','watched','priority','netflix','prime')


# class MovieDeleteView(DeleteView):
#     model = Movie
#     success_url = reverse_lazy('movie-add')


# class MovieDetailView(DetailView):
#     """
#     This one works: http://127.0.0.1:8000/movie/movie/tt21469794/
#     """
#     model = Movie
#     fields = ('ttnumber','watched','priority','netflix','prime')


# class MovieListView(ListView):
#     """
#     works: http://127.0.0.1:8000/movie/movie/list/
#     """
#     model = Movie

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