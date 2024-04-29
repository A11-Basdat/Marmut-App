from django.urls import path
from authentication.views import register

app_name = 'authentication'

urlpatterns = [
    path('authentication/', register, name='authentication'),
]