from rest_framework import serializers

from apps.cinema.models import *


class PerformanceTimeSerializer(serializers.ModelSerializer):

    time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = PerformanceTime

        fields = [
            'time'
        ]


class MovieDateBuildingVersionScheduleSerializer(serializers.ModelSerializer):

    schedule = PerformanceTimeSerializer(many=True, read_only=True)

    class Meta:
        model = MovieDateBuildingVersionSchedule

        fields = [
            'version',
            'language',
            'schedule'
        ]


class MovieDateBuildingSerializer(serializers.ModelSerializer):

    versions = MovieDateBuildingVersionScheduleSerializer(
        many=True, read_only=True)

    class Meta:
        model = MovieDateBuilding

        fields = [
            'building',
            'versions'
        ]
        depth = 1


class MovieDateSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y')
    buildings = MovieDateBuildingSerializer(many=True, read_only=True)

    class Meta:
        model = MovieDate

        fields = [
            'date',
            'buildings'
        ]


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    dates = MovieDateSerializer(many=True, read_only=True)

    def get_image(self, obj):
        return obj.image.url 
    
    class Meta:
        model = Movie

        fields = [
            'id',
            'get_absolute_url',
            'name',
            'genres',
            'duration',
            'description',
            'image',
            'clicked',
            'dates'
        ]

class SimpleMovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url 
    
    class Meta:
        model = Movie

        fields = [
            'id',
            'get_absolute_url',
            'name',
            'genres',
            'duration',
            'description',
            'image',
            'clicked',
        ]

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City

        fields = [
            'name',
        ]


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building

        fields = [
            'name',
        ]


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre

        fields = [
            'name',
        ]
