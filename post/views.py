import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post


# Create your views here.
@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            content=content,
            image=image,
            poster=user,
        )
        return redirect('index')

    return render(request, 'post/create.html')


@login_required
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/detail.html', {'post': post})


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

    return render(request, 'post/update.html', {'post': post})


@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('index')
