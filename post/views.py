from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username, email, password)
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
        
        if user is None:
            return render(request, 'signin.html', {'error': 'メールアドレスまたは、パスワードが違います。'})

        return redirect('index')
    else:
        return render(request, 'signin.html')


def index(request):
    return render(request, 'index.html')
