from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movie_reviews'

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('add/', views.AddMovieView.as_view(), name="movie-add"),
    path('details/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
]