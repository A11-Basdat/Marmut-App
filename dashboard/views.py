from django.shortcuts import render, redirect
from django.db import connection
from base.helper.function import parse
from dashboard.query import *
# def dashboard(request):
#     return render(request, 'dashboard.html')

def dashboard(request):
    context = {}
    if request.session['is_label']:
        cursor = connection.cursor()
        query = get_label_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_podcaster']:
        cursor = connection.cursor()
        query = get_podcaster_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_artist']:
        cursor = connection.cursor()
        query = get_artist_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_songwriter']:
        cursor = connection.cursor()
        query = get_songwriter_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_penggunabiasa']:
        cursor = connection.cursor()
        query = get_penggunabiasa_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]

    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT k.judul, k.durasi, k.id
        FROM KONTEN as k, PODCAST as p
        WHERE k.id = p.id_konten
    """)

    res = cursor.fetchall()

    podcast_list = [{
    'title': title,
    'duration': duration,
    'id': str(id)
    } for title, duration, id in res]

    context['all_podcasts'] = podcast_list

    print(context)

    return render(request, 'dashboard.html', context)

def search_bar(request):
    return render(request, 'search_bar.html')