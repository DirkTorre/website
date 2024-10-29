from django.contrib import admin
from django.urls import path
from . import views

app_name = "movie_reviews"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("add/", views.AddMovieView.as_view(), name="movie-add"),
    path("details/<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path(
        "details/<int:pk>/review/add/",
        views.MovieReviewCreateView.as_view(),
        name="review-add",
    ),
    path(
        "reviews/<int:pk>/update/",
        views.MovieReviewUpdateView.as_view(),
        name="review-update",
    ),
    path(
        "reviews/<int:pk>/delete/",
        views.MovieReviewDeleteView.as_view(),
        name="review-delete",
    ),
    path("list/", views.MovieStatusListView.as_view(), name="movie-list"),
    path("download/", views.DownloadIMDbDataView.as_view(), name="imdb-download"),
    path(
        "download/progress/", views.DownloadProgressView.as_view(), name="imdb-convert"
    ),
]
