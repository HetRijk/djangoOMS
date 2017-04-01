# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#Views are Python functions that take a request from the user and
# give back a response

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is the music app homepage</h1>')
