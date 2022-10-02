from django.urls import path, include

from cinema import views

urlpatterns = [
    path('movies-list/', views.MoviesList.as_view()),
    path('movie-details/<int:pk>', views.MovieDetails.as_view()),
    path('hottest-movies/', views.HottestMoviesList.as_view()),
    path('buildings-list/', views.BuildingsList.as_view()),
    path('genres-list/', views.GenresList.as_view()),
    path('cities-list/', views.CitiesList.as_view())
]
