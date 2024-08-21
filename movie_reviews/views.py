from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.contrib import messages

from .forms import AddWatchedMovieForm, AddUnwatchedMovieForm

from .models import WatchedStatus, WatchedDates, Availability

from .signals import check_watched_status_change


class HomePageView(TemplateView):
    template_name = 'movie_reviews/index.html'

    def get_context_data(self, *args, **kwargs):
        # context = super(self).get_context_data(*args, **kwargs)
        context = {}
        context['message'] = 'KILL THE CARDASHIANS'
        return context


class AddWatchedMovieView(FormView):
    template_name = "movie_reviews/add_watched_movie.html"
    form_class = AddWatchedMovieForm
    success_url = "/movies/adddata/watched/"

    def form_valid(self, form):
        # Get cleaned data
        id = form.cleaned_data["imdb_id"]
        date = form.cleaned_data["date"]
        enjoyment = form.cleaned_data["enjoyment"]
        netflix = form.cleaned_data["netflix"]
        prime = form.cleaned_data["prime"]

        
        # Create or update WatchedStatus
        watched_status_obj, created = WatchedStatus.objects.update_or_create(
            # attributes to search for
            tconst = id,        
            defaults= {
                # attributes to update
                'status': True,
                'priority': False}
        )

        # Add watched date
        if date:
            WatchedDates.objects.create(
                tconst = watched_status_obj,
                watch_date = date,
                enjoyment = int(enjoyment)
            )

        # Update Netflix status
        if netflix is not None:
            Availability.objects.update_or_create(
                tconst = watched_status_obj,
                defaults = {"netflix": netflix}
            )

        # Update Prime status
        if prime is not None:
            Availability.objects.update_or_create(
                tconst = watched_status_obj,
                defaults = {"prime": prime}
            )

        if created:
            # if a new movie is added
            messages.success(self.request,
                             f'Successfully added {watched_status_obj.tconst}')
        else:
            # if a movie is updated
            print(check_watched_status_change(watched_status_obj))
            messages.success(self.request,
                             f'Successfully updated {watched_status_obj.tconst}')
            
            

        return super().form_valid(form)


class AddUnwatchedMovieView(FormView):
    template_name = "movie_reviews/add_unwatched_movie.html"
    form_class = AddUnwatchedMovieForm
    success_url = "/movies/adddata/unwatched/"

    def form_valid(self, form):
        # Extract cleaned data from the form
        imdb_id = form.cleaned_data["imdb_id"]
        priority = form.cleaned_data["priority"]
        netflix = form.cleaned_data["netflix"]
        prime = form.cleaned_data["prime"]

        # Check if the movie already exists in WatchedStatus
        watched_status_obj, created = WatchedStatus.objects.get_or_create(
            tconst = imdb_id,
            defaults = {'status': False, 'priority': priority}
        )

        if created:
            # If the movie was newly created, add its availability
            Availability.objects.create(
                tconst = watched_status_obj,
                netflix = netflix,
                prime = prime
            )
        else:
            # Update availability if the movie already exists
            availability, created = Availability.objects.get_or_create(tconst=watched_status_obj)
            if netflix is not None:
                availability.netflix = netflix
            if prime is not None:
                availability.prime = prime
            availability.save()

            # Update priority if the new value is True
            if priority:
                watched_status_obj.priority = True
                watched_status_obj.save()

        message = ''
        # TODO: update this code block so it works for availability, priority and created
        # TODO: transfer this functionality to the database model
        if created:
            # if a new movie is added
            message = f'Successfully added {watched_status_obj.tconst}'
        else:
            message += 'Successfully updated: '
            if watched_status_obj.changed_status():
                message += 'status; '
            if watched_status_obj.changed_priority():
                message += 'priority; '
        
        messages.success(self.request, message)

        messages.success(self.request, f'Successfully added {watched_status_obj.tconst}')

        return super().form_valid(form)


class WatchedStatusDetailView(DetailView):
    template_name = "movie_reviews/movie_detail.html"
    model = WatchedStatus

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        watchedstatus_id = self.kwargs.get('pk')  # Assuming 'pk' is the URL parameter
        context['watchedstatus'] = WatchedStatus.objects.get(pk=watchedstatus_id)
        return context



























# TODO: remove when site is done
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