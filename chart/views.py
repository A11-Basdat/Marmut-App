from django.shortcuts import render

def list_chart(request):
    return render(request, "listChart.html")

def detail_chart(request):
    return render(request, "detailChart.html")
