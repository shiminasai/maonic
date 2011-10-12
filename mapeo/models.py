# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from lugar.models import Municipio
from thumbs import ImageWithThumbsField
from smart_selects.db_fields import ChainedForeignKey

#Galeria de foto.
FOTOS_SIZES = ((640, 480), (227, 154))

class SelectorBase(models.Model):
    '''modelo abstracto para semilla, materia, 
    buenas practicas, organizacion, certificacion, rubros'''
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ['nombre'] 

class RubroCultivo(SelectorBase):
    pass

class RubroArboles(SelectorBase):
    pass

class RubroAnimales(SelectorBase):
    pass

class Rubros(SelectorBase):
    pass

class Semilla(SelectorBase):
    pass

class MateriaProcesada(SelectorBase):
    pass

class BuenasPracticas(SelectorBase):
    pass

class TipoOrganizacion(SelectorBase):
    pass

class Certificacion(SelectorBase):
    pass

class AreaTrabajo(SelectorBase):
    pass

class FichaBaseProductores(models.Model):
    """Modelo abstracto para Familias y Promotores"""
    nombre = models.CharField('Nombre', max_length=150)
    direccion = models.TextField()
    municipio = models.ForeignKey(Municipio)
    lat = models.DecimalField(blank=True, max_digits=8,
            decimal_places=2, verbose_name='latitud', null=True)
    lon = models.DecimalField(blank=True, max_digits=8,
            decimal_places=2, verbose_name='longitud', null=True)
    telefono = models.CharField(max_length='8', blank=True, null=True)
    celular = models.CharField(max_length='8', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)

    # Campos de control de seguridad
    user = models.ForeignKey(User) #Usuario que creó el registro
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now_add=True)

    # Rubros comunes
    arboles = models.ManyToManyField(RubroArboles, blank=True)
    animales = models.ManyToManyField(RubroAnimales, blank=True)
    cultivos = models.ManyToManyField(RubroCultivo, blank=True)
    semillas = models.ManyToManyField(Semilla, blank=True)
    materia_procesada = models.ManyToManyField(MateriaProcesada, blank=True)
    certificacion = models.ManyToManyField(Certificacion, blank=True)
    buenas_practicas = models.ManyToManyField(BuenasPracticas, blank=True)

    #Fotos
    foto1 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto2 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto3 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto4 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto5 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ['nombre']

class FichaBaseAsociaciones(models.Model):
    """Modelo Abstracto para Asociaciones, Uniones y Centrales de Cooperativas"""
    nombre = models.CharField('Nombre', max_length=150)
    fecha_est = models.DateField('fecha de establecimiento', blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    municipio = models.ForeignKey(Municipio)
    lat = models.DecimalField(blank=True, max_digits=8,
            decimal_places=2, verbose_name='latitud', null=True)
    lon = models.DecimalField(blank=True, max_digits=8,
            decimal_places=2, verbose_name='longitud', null=True)
    telefono = models.CharField(max_length=8, blank=True, null=True)
    celular = models.CharField(max_length=8, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    representante_legal = models.CharField(max_length=100, blank=True, null=True)
    representante_tecnico = models.CharField(max_length=100, blank=True, null=True)
    num_hombres = models.IntegerField('numero de miembros hombres', blank=True, null=True)
    num_mujeres = models.IntegerField('numero de miembros mujeres', blank=True, null=True)

    # Campos de control y seguridad
    user = models.ForeignKey(User) #usuario que creó el registro
    tipo_org = models.ForeignKey(TipoOrganizacion, blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)

    # Rubros comunes
    rubros = models.ManyToManyField(Rubros, blank=True)
    semillas = models.ManyToManyField(Semilla, blank=True)
    materia_procesada = models.ManyToManyField(MateriaProcesada, blank=True)
    certificacion = models.ManyToManyField(Certificacion, blank=True)
    area_trabajo = models.ManyToManyField(AreaTrabajo, blank=True)
 
    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ['nombre']

class FichaBaseEmpresas(models.Model):
    """Modelo Abstracto para Financieras, comercializadoras, comerciales y certificadoras"""
    nombre = models.CharField('Nombre', max_length=150)
    direccion = models.TextField()
    municipio = models.ForeignKey(Municipio)
    lat = models.DecimalField(blank=True, max_digits=8, 
            decimal_places=2, verbose_name='latitud', null=True)
    lon = models.DecimalField(blank=True, max_digits=8, 
            decimal_places=2, verbose_name='longitud', null=True)
    telefono = models.CharField(max_length=8, blank=True, null=True) 
    celular = models.CharField(max_length=8, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    
    # Campos de control y seguridad
    user = models.ForeignKey(User) #usuario que lo creo
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)
   
    # Rubros Comunes
    animales = models.ManyToManyField(RubroAnimales, blank=True)
    cultivos = models.ManyToManyField(RubroCultivo, blank=True)
    semillas = models.ManyToManyField(Semilla, blank=True)
    materia_procesada = models.ManyToManyField(MateriaProcesada, blank=True)
    certificacion = models.ManyToManyField(Certificacion, blank=True)
   
    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ['nombre']

class Centrales(FichaBaseAsociaciones):
    num_asociaciones = models.IntegerField('número de asociaciones agrupadas')
    num_cooperativas= models.IntegerField('número de cooperativas agrupadas')

    class Meta:
        verbose_name_plural = 'centrales'
        verbose_name = 'central'

class Uniones(FichaBaseAsociaciones):
    num_cooperativas= models.IntegerField('número de cooperativas agrupadas')

    class Meta:
        verbose_name_plural = 'uniones'
        verbose_name = 'unión'

class Cooperativa(FichaBaseAsociaciones):
    # FIXME: El modelos debe ser dinámico: Centrales\Uniones
    nombre_org = ChainedForeignKey(
            Centrales,
            chained_field='tipo_org',
            chained_model_field='tipo_org',
            show_all=False,
            auto_choose=True,
            blank=True,
            null=True
    )

    class Meta:
        verbose_name_plural = 'cooperativas'
        verbose_name = 'cooperativa'
 
class Familia(FichaBaseProductores):
    nombre_finca = models.CharField('Nombre de finca', max_length=50)
    area_finca = models.DecimalField('Area de la finca en Manzanas', 
            decimal_places=2, max_digits=8)
    tipo_org = models.ForeignKey(TipoOrganizacion)
    # FIXME: El modelos debe ser dinámico: Cooperativa\Uniones???
    nombre_org = ChainedForeignKey(
            Cooperativa,
            chained_field='tipo_org',
            chained_model_field='tipo_org',
            show_all=False,
            auto_choose=True,
            blank=True,
            null=True
    ) 

    def __unicode__(self):
        return '%s - %s' % (self.nombre_finca, self.nombre)

class AsistenciaTecnica(FichaBaseProductores):
    desde= models.IntegerField('desde cuando provee asistencia')
    promedio = models.IntegerField('promedio de fincas atendidas por año')
    tipo_org = models.ForeignKey(TipoOrganizacion)
    # FIXME: El modelos debe ser dinámico: Cooperativa\Centrales\Uniones
    nombre_org = ChainedForeignKey(
            Cooperativa,
            chained_field='tipo_org',
            chained_model_field='tipo_org',
            show_all=False,
            auto_choose=True,
            null=True
    )

    class Meta:
        verbose_name_plural = 'Agentes de asistencia técnica'
        verbose_name = 'Agente de asistencia técnica'

class ComInsumo(FichaBaseEmpresas):
    desde_insumo = models.IntegerField('desde cuando provee insumo')
    promedio = models.IntegerField('promedio de clientes atendidos por año')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion) #TODO: Este campo va???

    class Meta:
        verbose_name_plural = 'Empresas comercializadora de insumos'
        verbose_name = 'Empresa comercializadora de insumos'

class ComProducto(FichaBaseEmpresas):
    desde = models.IntegerField('desde cuando comercializa')
    promedio = models.DecimalField('promedio de volumen de negocio en US$ por año', 
            decimal_places=2, max_digits=8)
    tipo_prov = models.ManyToManyField(TipoOrganizacion) #TODO: Este campo va???

    class Meta:
        verbose_name_plural = 'Empresas comercializadora de productos'
        verbose_name = 'Empresa comercializadora de productos'

class Certificadora(FichaBaseEmpresas):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones por año')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion) #TODO: Este campo va???

    class Meta:
        verbose_name_plural = 'Empresas certificadora'
        verbose_name = 'Empresa certificadora'

class Financiera(FichaBaseEmpresas):
    desde = models.IntegerField('desde cuando financian')
    promedio = models.IntegerField('promedio de número de clientes por año')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion) #TODO: Este campo va???

class OrgPublica(FichaBaseEmpresas):
    representante = models.CharField(max_length=100)
    representante_tecnico = models.CharField('representante técnico enlace con MAONIC', max_length=100)

    class Meta:
        verbose_name_plural = 'Organizaciones Pública'
        verbose_name = 'Organización Pública'
