from django.contrib import admin
from django.urls import path
from galeria.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
