# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request, 'session_words/index.html')

def process(request):
    new_word = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "big":
            new_word[key] = value
        if key == 'big':
            new_word['big'] = 'big'
        else:
            new_word['big'] = ''
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []
       
    temp = request.session['words']
    temp.append(new_word)
    request.session['words'] = temp
    return redirect('/')

def reset(request):
    while 'words' in request.session:
        request.session.pop('words')
    return redirect('/')