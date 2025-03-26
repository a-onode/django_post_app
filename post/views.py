import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

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


@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']

        Post.objects.create(
            title=title,
            content=content,
            image=image,
            poster=user,
        )
        return redirect('index')

    return render(request, 'create.html')


@login_required
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})


@login_required
def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        delete_image = request.POST.get('delete_image')

        post.title = title
        post.content = content
        if image:
            if post.image:
                os.remove(post.image.path)
            post.image = image
        elif delete_image == 'on':
            if post.image:
                os.remove(post.image.path)
            post.image = None
        post.save()
        return redirect('detail', id=post.id)

    return render(request, 'update.html', {'post': post})


@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('index')
