from django.shortcuts import render, redirect

def dashboard(request):
    return render(request, 'dashboard.html')

def search_bar(request):
    return render(request, 'search_bar.html')