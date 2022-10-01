from rest_framework import serializers

from .models import *


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieBuildingDateTimes

        fields = [
            'performance_times'
        ]


class DateSerializer(serializers.ModelSerializer):

    schedule = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = MovieBuildingDate

        fields = [
            'date',
            'schedule'
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
            'genres',
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

        fields = [
            'name',
        ]


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre

        fields = [
            'name',
        ]
