from django.shortcuts import render
from django.db import connection

def pembayaran_paket(request):
    return render(request, "pembayaran_paket.html")

def riwayat_transaksi(request): 
    return render(request, "riwayat_transaksi.html")

def langganan_paket(request):
    cursor = connection.cursor()
    cursor.execute(f"""
            SELECT * FROM PAKET
    """)
    results = cursor.fetchall()
    context = {
        'results': results
    }
    return render(request, "langganan_paket.html", context)