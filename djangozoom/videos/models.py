# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.
from django.db import models
from django.shortcuts import render
class Videos(models.Model):
    meetings = models.CharField(max_length=30)
    download_url = models.URLField()
    archivo = 'static/datos.json'

class Webinar(models.Model):

    pass

    curso = models.CharField(max_length=12)
    inicio = models.DateTimeField(verbose_name="fecha de inicio")
    fin_curso = models.DateTimeField(blank=None)

    def contenido(request):

        template = "contenido.html"

        with open('static/datos.json') as json_data:
            data = json.load(json_data)

            sub = data['meetings']

        context = {
            "tabla": data['meetings'],
            "tabla2": sub[0]
        }

        return render(request, template, context)
