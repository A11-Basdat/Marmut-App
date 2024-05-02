from django.shortcuts import render, redirect

def userplaylist(request):
    return render(request, 'userplaylist.html')

def addplaylist(request):
    return render(request, 'addplaylist.html')

