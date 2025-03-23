from django.contrib import admin
from django.urls import path

from .views import signup, signin, signout, index, detail, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('index/', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
]
