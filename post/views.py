from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import Post


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(
                request,
                'signup.html',
                {'error': 'このユーザーは既に登録されています。'},
            )
        else:
            return redirect('signin')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(
                request,
                'signin.html',
                {'error': 'メールアドレスまたは、パスワードが違います。'},
            )
    else:
        return render(request, 'signin.html')


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
