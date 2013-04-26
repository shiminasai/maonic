# -*- coding: UTF-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from models import *

class NoticiasAdmin(admin.ModelAdmin, AdminImageMixin):
	search_fields = ['titulo']
	date_hierarchy = 'fecha'

admin.site.register(Noticias, NoticiasAdmin)