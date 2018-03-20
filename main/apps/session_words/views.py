# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from datetime import datetime

words = []
def index(request):
    print words
    return render(request, "session_words/index.html")
def add(request):
    content = {
        "word": request.POST['word'],
        "timestamp": datetime.now().strftime('%I:%M:%S%p, %b %d %Y'),
        "fontsize": request.POST.get("bigfonts"),
        "color": request.POST.get('color')
    }
    
    if request.method == "POST":
        word = request.POST['word']
        color = request.POST.get('color')
        words.append(content)
        request.session['words'] = words

        return redirect("/")
def clear(request):
    if request.method == "POST":
        if len(words) != 0:
            for item in range(0,len(words)):
                words.pop()
        request.session["words"] = words
        return redirect("/")
