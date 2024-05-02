from django.urls import path
from dashboard.views import dashboard, search_bar

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('search_bar/', search_bar, name='search_bar')
]