from django.contrib import admin
from django.urls import path

from .views import signup, signin, signout, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('index/', index, name='index'),
]
