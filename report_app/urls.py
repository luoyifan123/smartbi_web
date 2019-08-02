from django.conf.urls import url
from report_app.views import views
from report_app.views import report


urlpatterns = [
    url(r'^report1$', views.report),
    url(r'^table$', report.get_table),
    url(r'^json', report.get_json)
]