from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

# apps base urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('db_api.urls')),
]
