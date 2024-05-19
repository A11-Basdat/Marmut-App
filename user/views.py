from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from datetime import datetime, timedelta

import uuid

def uuid_generate_v4():
    generated_uuid = uuid.uuid4()
    return str(generated_uuid).lower()

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

def pembayaran_paket(request, jenis):
    if 'email' not in request.session:
        return redirect('/authentication/login/')
    
    email = request.session['email']
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        cursor = connection.cursor()
        cursor.execute("SELECT jenis, harga FROM PAKET WHERE jenis = %s", [jenis])
        paket = cursor.fetchone()

        if paket:
            timestamp_dimulai = datetime.now()
            timestamp_berakhir = timestamp_dimulai + timedelta(days=30)  

            cursor.execute("""
                INSERT INTO TRANSACTION (id, jenis_paket, email, timestamp_dimulai, timestamp_berakhir, metode_bayar, nominal)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, [uuid_generate_v4(), paket[0], email, timestamp_dimulai, timestamp_berakhir, payment_method, paket[1]])

            cursor.execute("""
                INSERT INTO premium (email)
                VALUES (%s)
            """, [email])

            messages.success(request, 'Pembayaran berhasil!')
            return redirect('/dashboard')  

    cursor = connection.cursor()
    cursor.execute("SELECT jenis, harga FROM PAKET WHERE jenis = %s", [jenis])
    results = cursor.fetchone()
    context = {
        'jenis': results[0],
        'harga': results[1]
    }
    return render(request, "pembayaran_paket.html", context)

def riwayat_transaksi(request): 
    if 'email' not in request.session:
        return redirect('/authentication/login/')
    email = request.session['email']
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM TRANSACTION
        WHERE email = %s
    """, [email])
    results = cursor.fetchall()
    context = {
        'results': results
    }
    return render(request, "riwayat_transaksi.html", context)

