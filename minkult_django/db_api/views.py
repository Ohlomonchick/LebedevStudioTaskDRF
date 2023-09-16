from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework import filters


from .models import *
from .serializers import *


class ComposerViewSet(viewsets.ModelViewSet):
    serializer_class = ComposerSerializer
    queryset = Composer.objects.all()

    # allows to search records using model parameters
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "genre_id"
    lookup_value_regex = "[^/]+"    # this allows to access records genre/{genre_id} where genre_id is str "int.int"

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class TextAuthorViewSet(viewsets.ModelViewSet):
    serializer_class = TextAuthorSerializer
    queryset = TextAuthor.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    # in order to allow song records filtering by fields
    filterset_fields = ['name', "creation_year", "genre", "theme", "composer", "text_author"]

    # in songs search also uses keywords
    search_fields = ['name', 'keywords']





