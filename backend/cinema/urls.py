from django.urls import path, include

from cinema import views

urlpatterns = [
    path('latest-movies/', views.LatestMoviesList.as_view()),
    path('latest-buildings/', views.LatestBuildingsList.as_view()),
]