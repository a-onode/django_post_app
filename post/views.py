from django.shortcuts import render


# Create your views here.
def fn(request):
    return render(request, 'example.html', {'arg': 'hello world'})
