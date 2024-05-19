from django.urls import path
from chart.views import list_chart, detail_chart

app_name = 'chart'

urlpatterns = [
    path('', list_chart, name='list_chart'),
    path('detail/<uuid:chart_id>/', detail_chart, name='detail_chart'),
]