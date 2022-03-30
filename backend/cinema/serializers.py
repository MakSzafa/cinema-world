from rest_framework import serializers

from .models import *

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule

        fields = [
            'time'
        ]

class DateSerializer(serializers.ModelSerializer):

    performance_times = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Date

        fields = [
            'date',
            'performance_times'
        ]

class MovieBuildingSerializer(serializers.ModelSerializer):

    dates = DateSerializer(many=True, read_only=True)

    class Meta:
        model = MovieBuilding

        fields = [
            'building',
            'dates'
        ]
        depth = 1 
        

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