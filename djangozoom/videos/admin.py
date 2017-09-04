# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Videos
from .models import Webinar

admin.site.register(Videos)
admin.site.register(Webinar)