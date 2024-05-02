from django.urls import path
from chart.views import list_chart

app_name = 'chart'

urlpatterns = [
    path('', list_chart, name='list_chart'),
]