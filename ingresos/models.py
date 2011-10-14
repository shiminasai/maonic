# -*- coding: UTF-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.


class IngresoVendio(models.Model):
    nombre = models.CharField(max_length=150)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "A quien vendió"
        
class IngresoManeja(models.Model):
    nombre = models.CharField(max_length=150)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Quien maneja el negocio"
        
CHOICE_CATEG = (
                 (1,"Agroforestales"),
                 (2,"Forestales"),
                 (3,"Granos básicos"),
                 (4,"Ganado mayor"),
                 (5,"Animales de patio"),
                 (6,"Hortalizas y frutas"),
                 (7,"Musaceas"),
                 (8,"Raíces y tubérculos")
                     
                )

class RubrosI(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    categoria = models.IntegerField(choices=CHOICE_CATEG, null = True, blank = True)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "IngresoFamiliar-Rubros"
      
class IngresoFamiliar(models.Model):
    ''' Modelo Ingreso familiar. venta de rubros
    '''
    rubro = models.ForeignKey(RubrosI)
    cantidad = models.IntegerField('Cantidad vendida en el año pasado',null=True, blank=True)
    precio = models.IntegerField('Precio de venta por unidad C$',null=True, blank=True)
    quien_vendio = models.ForeignKey(IngresoVendio,verbose_name='¿A quien vendio?',null=True, blank=True)
    maneja_negocio = models.ForeignKey(IngresoManeja,verbose_name='¿Quién maneja el negocio',null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.rubro.nombre
    
    class Meta:
        verbose_name_plural = "Ingreso Familiar"

#-------------------------------------------------------------------------------

# Otros ingresos.

class Fuentes(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otros-Ingreso - Fuentes"

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otro-Ingreso - TipoTrabajo"
      
class OtrosIngresos(models.Model):
    '''Otros ingresos
    '''
    fuente = models.ForeignKey(Fuentes)
    tipo = models.ForeignKey(TipoTrabajo, null=True, blank=True)
    meses = models.IntegerField('# Meses que tiene ingreso',null=True, blank=True)
    ingreso = models.IntegerField('Ingreso por mes C$',null=True, blank=True)
    tiene_ingreso = models.ForeignKey(IngresoManeja,verbose_name="Quienes tiene el ingreso",null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.fuente.nombre
    
    class Meta:
        verbose_name_plural = "Otros ingresos"
