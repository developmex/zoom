# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def listado(request):
    archivo = read("static/data.json")
    data = archivo
    return JsonResponse(data)
