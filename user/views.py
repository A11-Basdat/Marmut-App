from django.shortcuts import render
from django.db import connection

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

def pembayaran_paket(request,jenis):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT jenis,harga FROM PAKET WHERE jenis = %s
    """, [jenis])
    results = cursor.fetchone()
    context = {
        'jenis': results[0],
        'harga': results[1]
    }
    return render(request, "pembayaran_paket.html", context)

def riwayat_transaksi(request): 
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT * FROM TRANSACTION
    """)
    results = cursor.fetchall()
    context = {
        'results' : results
    }
    return render(request, "riwayat_transaksi.html", context)

