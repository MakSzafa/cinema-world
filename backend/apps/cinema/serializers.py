from rest_framework import serializers

from apps.cinema.models import *


class MovieDateBuildingVersionScheduleSerializer(serializers.ModelSerializer):

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


class MovieDateSerializer(serializers.ModelSerializer):

    buildings = MovieDateBuildingSerializer(many=True, read_only=True)

    class Meta:
        model = MovieDate

        fields = [
            'date',
            'buildings'
        ]


class MovieSerializer(serializers.ModelSerializer):

    dates = MovieDateSerializer(many=True, read_only=True)

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
