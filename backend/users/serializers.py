from rest_framework import serializers

from .models import *

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData

        fields = [
            'user',
            'favourite_genres',
            'favourite_cinemas',
        ]