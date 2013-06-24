# -*- coding: UTF-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from models import *
from image_cropping import ImageCroppingMixin

class NoticiasAdmin(admin.ModelAdmin, AdminImageMixin):
	search_fields = ['titulo']
	date_hierarchy = 'fecha'

class fotoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class FotoInlineAdmin(admin.StackedInline):
	model = FotosPortadas
	extra = 1

class PortadaAdmin(ImageCroppingMixin, admin.ModelAdmin):
	inlines = [FotoInlineAdmin]

admin.site.register(Portada,PortadaAdmin)
admin.site.register(FotosPortadas, fotoAdmin)
admin.site.register(Noticias, NoticiasAdmin)