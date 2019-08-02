
from django.shortcuts import render
from report_app.views.vertica import get_data_json,get_data_total
from django.http.response import HttpResponse
import json

def get_table(request):

    # json = get_data_json()
    context = {'jsondata': 'json'}
    return render(request, './report/html/table.html', context)



def get_json(request):
    if request.method == "GET":
        rows = request.GET.get('rows')
        page = request.GET.get('page')

        rows = get_data_json(rows, page)
        total = get_data_total();
        json1 ={"total": total, "rows": rows}
        print(request.GET.get('rows'),request.GET.get('page'))
        return HttpResponse(json.dumps(json1), content_type='application/json;charset=utf-8')