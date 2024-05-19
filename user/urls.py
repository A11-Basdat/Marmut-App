from django.urls import path
from user.views import langganan_paket, riwayat_transaksi, pembayaran_paket

app_name = 'user'

urlpatterns = [
    path('langganan_paket/', langganan_paket, name='langganan_paket'),
    path('riwayat_transaksi/', riwayat_transaksi, name='riwayat_transaksi'),
    path('pembayaran_paket/<str:jenis>', pembayaran_paket, name='pembayaran_paket')
]