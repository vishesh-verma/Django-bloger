# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import blogs
from .models import login



# Register your models here.
admin.site.register(blogs)
admin.site.register(login)
