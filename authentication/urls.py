from django.urls import path
from authentication.views import register, login, pilih_register

app_name = 'authentication'

urlpatterns = [
    path('pilih_register/', pilih_register, name='pilih_register'),
    path('login/', login, name='login'),
    path('register/<str:user_type>/', register, name='register'),
]