from django.contrib.postgres import fields
from rest_framework import serializers

from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = (
        #     'id',
        #     'name',
        #     'building',
        #     'version',
        #     'genre',
        #     'duration',
        #     'language',
        #     'date_times',
        #     'description',
        #     'image',
        #     'get_absolute_url'
        # )