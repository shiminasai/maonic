# -*- coding: UTF-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"

class Manejo(models.Model):
    nombre = models.CharField('Tipo de manejo', max_length=200)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Tipo de manejo"
        
class CultivosFinca(models.Model):
    ''' indicador cultivos en la finca
    '''
    cultivos = models.ForeignKey(Cultivos)
    area =  models.FloatField('Área/Mz')
    manejo = models.ForeignKey(Manejo)
    total = models.FloatField('Producción')
    consumo = models.FloatField('Consumo')
    venta_libre = models.FloatField('Venta')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.cultivos.nombre
    
    class Meta:
        verbose_name_plural = "Cultivos en la finca"
