from django.shortcuts import render, redirect
from django.db import connection
from base.helper.function import parse
from royalti.query import *

def royalti(request):
    context = {}
    if request.session['is_label']:
        cursor = connection.cursor()
        query = get_label_royalti_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_artist']:
        cursor = connection.cursor()
        query = get_artist_royalti_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_songwriter']:
        cursor = connection.cursor()
        query = get_songwriter_royalti_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    return render(request, 'royalti.html', context)




