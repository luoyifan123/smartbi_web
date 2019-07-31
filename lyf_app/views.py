from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'helloword'
    return render(request, 'hello.html', context)

def base(request):
    return render(request,'base.html')
