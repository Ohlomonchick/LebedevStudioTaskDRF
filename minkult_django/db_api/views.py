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

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "genre_id"
    lookup_value_regex = "[^/]+"

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
    filterset_fields = ['name', "creation_year", "genre", "theme", "composer", "text_author"]
    search_fields = ['name', 'keywords']





