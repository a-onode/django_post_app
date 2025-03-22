from django.contrib import admin
from django.urls import path

from .views import fn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', fn),
]
