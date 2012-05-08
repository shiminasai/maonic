# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from models import *

class MaonicAdmin(admin.ModelAdmin):

    def queryset(self, request):
        if request.user.is_superuser or request.user.has_perm('mapeo.edit_all'):
            return self.model.objects.all()
        elif request.user.is_staff:
            return self.model.objects.filter(user=request.user)
        
    def get_form(self, request, obj=None, ** kwargs):

        if request.user.is_superuser:
            form = super(MaonicAdmin, self).get_form(request, ** kwargs)
        else:
            form = super(MaonicAdmin, self).get_form(request, ** kwargs)
        #    form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
        return form

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return instance

    exclude = ['user']
    filter_horizontal = ('arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class FamiliaAdmin(MaonicAdmin):
    filter_horizontal = ('arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'
    
    def get_form(self, request, obj=None, ** kwargs):
        form = super(FamiliaAdmin, self).get_form(request, ** kwargs)
        form.base_fields['tipo_org'].queryset = TipoOrganizacion.objects.filter(id__in=[1, 2, 5])
        return form
    
    class Media:
        js = ['/files/js/familia.js', ]

class AsistenciaTecnicaAdmin(MaonicAdmin):
    filter_horizontal = ('arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'

class CooperativaAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo', 'rubros', 'semillas','materia_procesada','certificacion')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'
    
    def get_form(self, request, obj=None, ** kwargs):
        form = super(CooperativaAdmin, self).get_form(request, ** kwargs)
        form.base_fields['tipo_org'].queryset = TipoOrganizacion.objects.filter(id__in=[3, 4])
        return form
    
    class Media:
        js = ['/files/js/cooperativa.js', ]
    
class AsociacionAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo', 'rubros', 'semillas','materia_procesada','certificacion')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'
    
    def get_form(self, request, obj=None, ** kwargs):
        form = super(AsociacionAdmin, self).get_form(request, ** kwargs)
        form.base_fields['tipo_org'].queryset = TipoOrganizacion.objects.filter(id__in=[4])
        return form

class CentralesAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo', 'rubros', 'semillas','materia_procesada','certificacion')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'

class UnionesAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo', 'rubros', 'semillas','materia_procesada','certificacion')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'

class ComInsumoAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_cliente','animales','cultivos','semillas','materia_procesada','certificacion')
    
class ComProductoAdmin(MaonicAdmin):
    filter_horizontal = ('animales','cultivos','semillas','materia_procesada','certificacion')
    
class CertificadoraAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_cliente','animales','cultivos','semillas','materia_procesada','certificacion')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'

class FinancieraAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_cliente','animales','cultivos','semillas','materia_procesada','certificacion')
    search_fields = ['nombre','user__username', 'municipio__nombre']
    list_filter = ['user', ]
    list_display = ['nombre','user','municipio',]
    date_hierarchy = 'fecha_agregado'
    
class OrgPublicaAdmin(MaonicAdmin):
    filter_horizontal = ('animales','cultivos','semillas','materia_procesada','certificacion')

#admin.site.register(Familia, MaonicAdmin)
admin.site.register(Familia, FamiliaAdmin)

#admin.site.register(Cooperativa, MaonicAdmin)
admin.site.register(Cooperativa, CooperativaAdmin)

admin.site.register(Asociacion, AsociacionAdmin)

admin.site.register(Uniones,UnionesAdmin)

#admin.site.register(Centrales, MaonicAdmin)
admin.site.register(Centrales,CentralesAdmin)

#admin.site.register(AsistenciaTecnica, MaonicAdmin)
admin.site.register(AsistenciaTecnica,AsistenciaTecnicaAdmin)

#admin.site.register(ComInsumo, MaonicAdmin)
admin.site.register(ComInsumo,ComInsumoAdmin)

#admin.site.register(ComProducto, MaonicAdmin)
admin.site.register(ComProducto,ComProductoAdmin)

#admin.site.register(Certificadora, MaonicAdmin)
admin.site.register(Certificadora,CertificadoraAdmin)

#admin.site.register(Financiera, MaonicAdmin)
admin.site.register(Financiera,FinancieraAdmin)

#admin.site.register(OrgPublica, MaonicAdmin)
admin.site.register(OrgPublica,OrgPublicaAdmin)

admin.site.register(RubroCultivo)
admin.site.register(RubroArboles)
admin.site.register(RubroAnimales)
admin.site.register(Rubros)
admin.site.register(Semilla)
admin.site.register(MateriaProcesada)
admin.site.register(BuenasPracticas)
admin.site.register(TipoOrganizacion)
admin.site.register(Certificacion)
admin.site.register(AreaTrabajo)
