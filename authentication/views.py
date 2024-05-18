import datetime
import re
import uuid
from django.shortcuts import render, redirect
from django.db import connection, InternalError
from django.contrib import messages
from base.helper.function import parse
from authentication.forms import *
from authentication.constant import *
from authentication.query import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        query = get_user_query(email, password)
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        request.session['is_penggunabiasa'] = False
        request.session['is_podcaster'] = False
        request.session['is_artist'] = False
        request.session['is_songwriter'] = False
        request.session['is_label'] = False
        if len(res) == 1:
            akun = res[0]
            for attr in akun:
                if isinstance(akun[attr], uuid.UUID):
                    request.session[attr] = str(akun[attr])
                elif isinstance(akun[attr], datetime.date):
                    date = datetime.datetime.strptime(str(akun[attr]), '%Y-%m-%d')
                    formatted_date = date.strftime('%d %B %Y')
                    request.session[attr] = formatted_date
                else:
                    request.session[attr] = akun[attr]
            request.session[SESSION_ROLE_KEYS[akun['user_role']]] = True
            return redirect('/dashboard/')
        else:
            messages.info(request,'Email atau Password salah')

    context = {'login_form': loginForm()}
    return render(request, 'login.html', context)

@csrf_exempt
def register_pengguna(request):
    if request.method == 'POST':
        if 'pengguna_submit' in request.POST:
            pengguna_form = registerPenggunaForm(request.POST)
            if pengguna_form.is_valid():
                email = pengguna_form.cleaned_data['email']
                password = pengguna_form.cleaned_data['password']
                nama = pengguna_form.cleaned_data['nama']
                tempat_lahir = pengguna_form.cleaned_data['tempat_lahir']
                tanggal_lahir = pengguna_form.cleaned_data['tanggal_lahir']
                kota_asal = pengguna_form.cleaned_data['kota_asal']
                gender = pengguna_form.cleaned_data['gender']
                role = pengguna_form.cleaned_data['role']
                query = check_user_query(email)
                cursor = connection.cursor()
                cursor.execute(query)
                res = parse(cursor)
                if len(res) != 0:
                    messages.info(request,'Email sudah ada!')
                else:
                    if role == 'podcaster':
                        payload = podcaster_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
                    elif role == 'artist':
                        payload = artist_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
                    elif role == 'songwriter':
                        payload = songwriter_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
                    else:
                        payload = penggunabiasa_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
                    if payload['success']:
                        return redirect('/authentication/login/')
                    else:
                        trimmed_string = re.sub(r'\(|\)|\'', '', payload['msg'])
                        message = re.search(r'\[([^]]+)\]', trimmed_string).group(1)
                        messages.info(request, message)
    context = {
        'pengguna_form': registerPenggunaForm(),
    }
    return render(request, 'registerPengguna.html', context)


@csrf_exempt
def register_label(request):
    if request.method == 'POST':
        if 'label_submit' in request.POST:
            label_form = registerLabelForm(request.POST)
            if label_form.is_valid():
                email = label_form.cleaned_data['email']
                password = label_form.cleaned_data['password']
                nama = label_form.cleaned_data['nama']
                kontak = label_form.cleaned_data['kontak']
                query = check_user_query(email)
                cursor = connection.cursor()
                cursor.execute(query)
                res = parse(cursor)
                if len(res) != 0:
                    messages.info(request,'Email sudah ada!')
                else:
                    payload = label_register(email, password, nama, kontak)
                    if payload['success']:
                        return redirect('/authentication/login/')
                    else:
                        trimmed_string = re.sub(r'\(|\)|\'', '', payload['msg'])
                        message = re.search(r'\[([^]]+)\]', trimmed_string).group(1)
                        messages.info(request, message)
    context = {
        'label_form': registerLabelForm(),
    }
    return render(request, 'registerLabel.html', context)

def penggunabiasa_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role):
    try:
        cursor = connection.cursor()
        akun_query = insert_akun_query(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
        cursor.execute(akun_query)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

def podcaster_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role):
    try:
        cursor = connection.cursor()
        akun_query = insert_akun_query(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
        cursor.execute(akun_query)
        podcaster_query = insert_podcaster_query(email)
        cursor.execute(podcaster_query)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

def artist_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role):
    try:
        id = uuid.uuid4()
        cursor = connection.cursor()
        akun_query = insert_akun_query(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
        cursor.execute(akun_query)
        artist_query = insert_artist_query(id, email)
        cursor.execute(artist_query)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

def songwriter_register(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role):
    try:
        id = uuid.uuid4()
        cursor = connection.cursor()
        akun_query = insert_akun_query(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role)
        cursor.execute(akun_query)
        songwriter_query = insert_songwriter_query(id, email)
        cursor.execute(songwriter_query)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

def label_register(email, password, nama, kontak):
    try:
        id = uuid.uuid4()
        cursor = connection.cursor()
        label_query = insert_label_query(id, nama, email, password, kontak)
        cursor.execute(label_query)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

def logout(request):
    if "id" in request.session:
        request.session.clear()
        request.session['is_penggunabiasa'] = False
        request.session['is_podcaster'] = False
        request.session['is_artist'] = False
        request.session['is_songwriter'] = False
        request.session['is_label'] = False
        return redirect('/')
    return redirect('/')


def pilih_register(request):
    return render(request, 'pilihRegister.html')