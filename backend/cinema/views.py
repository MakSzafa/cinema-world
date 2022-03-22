from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters

from .models import *
from .serializers import *


class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'buildings__building__name']


class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class HottestMoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.order_by('-clicked')[:3]
    serializer_class = MovieSerializer
