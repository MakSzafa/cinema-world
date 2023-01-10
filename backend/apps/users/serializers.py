from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(
        format='%H:%M %d.%m.%Y', read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ['id', 'url', 'email', 'favourite_genres',
                  'favourite_cinemas', 'registered_at']


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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['id'] = self.user.id

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
