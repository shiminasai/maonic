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

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor.widgets import CKEditorWidget

class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Portada,PortadaAdmin)
admin.site.register(FotosPortadas, fotoAdmin)
admin.site.register(Noticias, NoticiasAdmin)