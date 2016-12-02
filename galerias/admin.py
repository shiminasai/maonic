# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import Galeria, FotoGalerias

class FotoGaleriaInlines(admin.TabularInline):
      model = FotoGalerias
      max_num = 20
      extra = 1

class GaleriaAdmin(admin.ModelAdmin):
	inlines = [FotoGaleriaInlines]
	list_display = ('titulo', 'autor',)

admin.site.register(Galeria, GaleriaAdmin)