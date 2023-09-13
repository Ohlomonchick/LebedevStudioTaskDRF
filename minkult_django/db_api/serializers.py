from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import *


class ComposerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Composer
        fields = (
            "id",
            "name"
        )


class TextAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextAuthor
        fields = (
            "id",
            "name"
        )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
            "genre_id"
        )
        lookup_field = "genre_id"


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = (
            "id",
            "name"
        )


class SongSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    composer = ComposerSerializer(many=True)
    text_author = TextAuthorSerializer(many=True)

    class Meta:
        model = Song
        fields = (
            "id",
            "name",
            "composer",
            "creation_year",
            "text_author",
            "genre",
            "theme",
            "keywords",
        )
