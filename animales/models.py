# -*- coding: UTF-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.

class Animales(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Finca - Animales"

class ProductoAnimal(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Finca - Producto"

class AnimalesCantidad(models.Model):
    animales = models.ForeignKey(Animales)
    cantidad = models.FloatField()
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.animales.nombre
        
    class Meta:
        verbose_name_plural = "Cantidades de Animales"
        
class AnimalesFinca(models.Model):
    ''' Modelo animales en la finca
    '''
    produccion = models.ForeignKey(ProductoAnimal)
    total_produccion = models.IntegerField('Total producion por año', null=True)
    consumo = models.FloatField('Consumo')
    venta_libre = models.FloatField('Venta libre')
    venta_organizada = models.FloatField('Venta organizada')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.produccion.nombre
    
    class Meta:
        verbose_name_plural = "Produccion de los animales"
