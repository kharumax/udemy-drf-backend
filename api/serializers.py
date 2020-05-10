from rest_framework import serializers

from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id","title","description")
        read_only = ("id",)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id","stars","user","movie")
        read_only = ("id",)