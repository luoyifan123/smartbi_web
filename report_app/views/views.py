from django.shortcuts import render

# Create your views here.

from  django.http import HttpResponse

def report(request):
    return HttpResponse("111111")