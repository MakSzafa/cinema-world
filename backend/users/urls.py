from django.urls import path

from users import views

urlpatterns = [
    path('user-data/', views.UserData.as_view()),
]