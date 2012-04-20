from django.contrib import admin
from django.contrib.auth.models import User
#modelos relacionados del monitoreo
from models import *
from organizacion.models import *
from tierra.models import *
from animales.models import *
from cultivos.models import *
from opciones_agroecologico.models import *
from semilla.models import *
from suelo.models import *
from inversiones.models import *
from ingresos.models import *
from propiedades.models import *
from credito.models import *
from seguridad.models import *
from riesgo.models import *

from autocomplete_admin import FkAutocompleteAdmin
#Organizacion
class OrganizacionGremialInline(admin.TabularInline):
    model = OrganizacionGremial
    fields = ['socio', 'nombre', 'desde_socio','beneficio', 'miembro_gremial', 
              'desde_miembro','capacitacion', 'desde_capacitacion']
    extra = 1
    max_num = 1

class TenenciaInline(admin.TabularInline):
    model = Tenencia
    extra = 1
    max_num = 1
    
#Uso de tierra
class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = 8 

#Animales
class AnimalesCantidadInline(admin.TabularInline):
    model = AnimalesCantidad
    extra = 1
    
class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1

#cultivos
class CultivosFincaInline(admin.TabularInline):
    model = CultivosFinca
    extra = 1

#opciones de manejo agroecologico
class OpcionesManejoInline(admin.TabularInline):
    model= OpcionesManejo
    extra = 1

#uso de semilla
class UsoSemillaInline(admin.TabularInline):
    model = UsoSemilla
    extra = 1
        
#Suelo
class SueloInline(admin.TabularInline):
    model = Suelo
    extra = 1
    max_num = 1

class ManejoSueloInline(admin.TabularInline):
    model = ManejoSuelo
    fields = ['preparan','traccion','analisis','fertilizacion',
              'practica','obra']
    extra = 1
    max_num = 1
 
#Inversiones
class InversionesInline(admin.TabularInline):
    model = Inversion
    extra = 1
    

#Ingreso familiar
class IngresoFamiliarInline(admin.TabularInline):
    model = IngresoFamiliar
    extra = 1

#Otros ingresos
class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    
#Propiedades y bienes
class TipoCasaInline(admin.TabularInline):
    model = TipoCasa
    extra = 1
    max_num = 1
    can_delete = False
    
class DetalleCasaInline(admin.TabularInline):
    model = DetalleCasa
    extra = 1
    max_num = 1
    can_delete = False
    
class PropiedadesInline(admin.TabularInline):
    model = Propiedades
    extra = 1
    can_delete = False
    
class InfraestructuraInline(admin.TabularInline):
    model = Infraestructura
    extra = 1
    can_delete = False
    
class HerramientasInline(admin.TabularInline):
    model = Herramientas
    extra = 1
    can_delete = False
    
class TransporteInline(admin.TabularInline):
    model = Transporte
    extra = 1
    can_delete = False

class CreditoInline(admin.TabularInline):
    model = Credito
    fields = ['recibe','desde','quien_credito','ocupa_credito',
              'satisfaccion','dia']
    extra = 1
    max_num = 1  
    
#Seguridad alimentaria
class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    can_delete = False 
    
#Riesgos que hacen vulnerables las fincas
class VulnerableInline(admin.TabularInline):
    model = Vulnerable
    extra = 1
    can_delete = False

class RiesgosInline(admin.TabularInline):
    model = Riesgos
    extra = 1
    can_delete = False
             
class EncuestaAdmin(FkAutocompleteAdmin):
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
        
    def queryset(self, request):
        qs = super(EncuestaAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
        
    save_on_top = True
    actions_on_top = True
    exclude = ('usuario',)
    #raw_id_fields = ("productor",)
    related_search_fields = { 
                              'productor':('nombre',)
                              #'productor' :{'search': ('nombre',), 'related': ('nombre',)},
                            }
    inlines = [OrganizacionGremialInline,TenenciaInline,UsoTierraInline,AnimalesCantidadInline,
               AnimalesFincaInline,CultivosFincaInline,OpcionesManejoInline,UsoSemillaInline,
               SueloInline,ManejoSueloInline,InversionesInline,IngresoFamiliarInline,
               OtrosIngresosInline,TipoCasaInline,DetalleCasaInline,PropiedadesInline,
               InfraestructuraInline,HerramientasInline,TransporteInline,CreditoInline,
               SeguridadInline,VulnerableInline,RiesgosInline
              ]
    list_display = ('productor','departamentos','finca','fecha',)
    #list_filter = ['productor__departamento__municipio']
    #search_fields = ['productor', 'productor__departamento__municipio']
    date_hierarchy = 'fecha'
    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }
    
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Recolector)
admin.site.register(OrgGremiales)
admin.site.register(BeneficiosObtenido)
admin.site.register(SerMiembro)
admin.site.register(Uso)
admin.site.register(Animales)
admin.site.register(ProductoAnimal)
admin.site.register(Cultivos)
admin.site.register(Manejo)
admin.site.register(CultivosVariedad)
admin.site.register(Variedades)
admin.site.register(Textura)
admin.site.register(Profundidad)
admin.site.register(Densidad)
admin.site.register(Pendiente)
admin.site.register(Drenaje)
admin.site.register(Preparar)
admin.site.register(Traccion)
admin.site.register(Fertilizacion)
admin.site.register(Conservacion)
admin.site.register(CultivosInversion)
admin.site.register(FuenteInversion)
admin.site.register(IngresoVendio)
admin.site.register(IngresoManeja)
admin.site.register(RubrosI)
admin.site.register(Fuentes)
admin.site.register(TipoTrabajo)
admin.site.register(Casa)
admin.site.register(Piso)
admin.site.register(Techo)
admin.site.register(Equipos)
admin.site.register(Infraestructuras)
admin.site.register(NombreHerramienta)
admin.site.register(NombreTransporte)
admin.site.register(DaCredito)
admin.site.register(OcupaCredito)
admin.site.register(Alimentos)
admin.site.register(Causa)
admin.site.register(Fenomeno)
admin.site.register(Graves)
admin.site.register(PreguntaRiesgo)
admin.site.register(ManejoAgro)
