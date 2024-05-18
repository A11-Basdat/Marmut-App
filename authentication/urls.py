from django.urls import path
from authentication.views import register_pengguna, register_label, login, pilih_register, logout

app_name = 'authentication'

urlpatterns = [
    path('pilih_register/', pilih_register, name='pilih_register'),
    path('login/', login, name='login'),
    path('register_pengguna/', register_pengguna, name='register_pengguna'),
    path('register_label/', register_label, name='register_label'),
    path('logout/', logout, name='logout')
]