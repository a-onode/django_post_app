from django.contrib import admin
from django.urls import path

from .views import signup, signin, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('index/', index, name='index'),
]
