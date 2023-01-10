from rest_framework import serializers

from django.conf import settings

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ['id', 'url', 'email', 'favourite_genres', 'favourite_cinemas', 'registered_at']


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'favourite_genres', 'favourite_cinemas']


class UserPasswordResetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']

class UserPasswordResetChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'password_reset_token']