# -*- coding: UTF-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.

class CultivosInversion(models.Model):
    nombre = models.CharField(max_length=150)
    def __unicode__(self):
        return self.nombre

class FuenteInversion(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
       
class Inversion(models.Model):
    cultivo = models.ForeignKey(CultivosInversion)
    area = models.FloatField('Area en Mz')
    comprado = models.FloatField('Insumos comprados C$')
    fabricado = models.FloatField('Insumos fabricados en finca C$')
    mano_obra = models.FloatField('Mano de obra familiar C$')
    contratado = models.FloatField('Mano de obra contratada C$')
    terreno = models.FloatField('Preparación de terreno C$')
    cosecha = models.FloatField('Cosesha y procesamiento C$')
    fuente = models.ForeignKey(FuenteInversion)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return self.cultivo.nombre
        
    class Meta:
        verbose_name_plural = "Inversiones en la finca"
