from django.urls import path

from users import views

urlpatterns = [
    path('profile/<int:pk>', views.Profile.as_view()),
]