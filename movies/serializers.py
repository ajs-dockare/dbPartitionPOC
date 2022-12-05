from rest_framework import serializers
from .models import Movie, Organisation
from django.contrib.auth.models import User


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')
    organisation = serializers.IntegerField(required=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator', 'organisation')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
