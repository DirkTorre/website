from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movie_reviews'

urlpatterns = [
    
    path('', views.HomePageView.as_view(), name="home"),
    path('adddata/watched/', views.AddWatchedMovieView.as_view(), name="add-watched"),
    path('adddata/unwatched/', views.AddUnwatchedMovieView.as_view(), name="add-unwatched"),
    path('<pk>/', views.WatchedStatusDetailView.as_view())
    # path('movie/list/', views.MovieListView.as_view(), name="movie-add"),
    # path('movie/add/', views.MovieCreateView.as_view(), name="movie-add"),
    # path('movie/<pk>/', views.MovieDetailView.as_view(), name="movie-detail"),
    # path('movie/<pk>/update/', views.MovieUpdateView.as_view(), name="movie-update"),
    # path('movie/<pk>/delete/', views.MovieDeleteView.as_view(), name="movie-delete"),
    # path('movie/', ) # main page
    # path('movie/<pk>/reviews/list/',) # lists reviews for a movie
    # path('movie/<pk>/reviews/add/',) # add review
    # path('movie/<pk>/reviews/update/',) # update review
    # path('movie/<pk>/reviews/delete/',) # delete review
]
