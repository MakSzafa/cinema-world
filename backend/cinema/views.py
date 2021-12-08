from re import T
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class LatestBuildingsList(APIView):
    def get(self, request, format=None):
        buildings = Building.objects.all()[0:4]
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)
class LatestMoviesList(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()[0:4]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)