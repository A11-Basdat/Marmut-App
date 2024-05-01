from django.shortcuts import render, redirect

def pilih_register(request):
    return render(request, 'pilihRegister.html')

def login(request):
    return render(request, 'login.html')

def register(request, user_type):
    return render(request, 'register.html', {'user_type': user_type})
