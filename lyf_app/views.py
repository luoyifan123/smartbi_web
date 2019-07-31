from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def hello(request):
    context = {'hello': 'helloWorld', 'hello2': 'hello2'}
    return render(request, 'hello.html', context)


def base(request):
    return render(request, 'base.html')
