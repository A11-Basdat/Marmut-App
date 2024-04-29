from django.shortcuts import render, redirect

def register(request):
    return render(request, 'register.html')