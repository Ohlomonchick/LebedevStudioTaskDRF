from django.urls import path, include
from rest_framework import routers
from db_api import views

router = routers.SimpleRouter()

# API handlers
router.register(r'song', views.SongViewSet, basename='song')
router.register(r'composer', views.ComposerViewSet, basename='composer')
router.register(r'genre', views.GenreViewSet, basename='genre')
router.register(r'text-author', views.TextAuthorViewSet, basename='text_author')


urlpatterns = [
    path('', include(router.urls)),
]