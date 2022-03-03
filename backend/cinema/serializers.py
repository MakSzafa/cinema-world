from django.contrib.postgres import fields
from rest_framework import serializers

from .models import *

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule

        fields = [
            'schedule'
        ]
        depth = 1

class DateSerializer(serializers.ModelSerializer):

    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Date

        fields = [
            'date',
            'schedules'
        ]

class MovieBuildingSerializer(serializers.ModelSerializer):

    dates = DateSerializer(many=True, read_only=True)

    class Meta:
        model = MovieBuilding

        fields = [
            'building',
            'dates'
        ]
        # zaleznie czy potrzeba informacji o budynku
        # depth = 1 
        

class MovieSerializer(serializers.ModelSerializer):

    buildings = MovieBuildingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie

        fields = [
            'id',
            'name',
            'genre',
            'duration',
            'description',
            'image',
            'clicked',
            'version',
            'language',
            'get_absolute_url',
            'buildings'
        ]
        
class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building

        fields = (
            'id',
            'name',
            'brand',
            'category',
            'city'
        )
