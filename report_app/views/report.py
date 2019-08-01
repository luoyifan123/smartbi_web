
from django.shortcuts import render

def get_table(request):
    context = {'hello': 'helloWorld', 'hello2': 'hello2'}
    return render(request, './report/html/table.html', context)
