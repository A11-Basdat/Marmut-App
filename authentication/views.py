from django.shortcuts import render, redirect

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')