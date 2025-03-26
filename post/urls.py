from django.urls import path

from .views import (
    signup,
    signin,
    signout,
    index,
    create,
    detail,
    update,
    delete
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('index/', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
