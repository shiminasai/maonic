# -*- coding: utf-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.

#cuales son los riesgos que hace la finca vulnerable

class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa"
        
class Fenomeno(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa + fenomeno"
        
class Graves(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - daños graves"
        
class Vulnerable(models.Model):
    ''' 20 modelo vulnerable
    '''
    motivo = models.ForeignKey(Fenomeno)
    respuesta = models.ManyToManyField(Graves, verbose_name="¿Cada cuanto hay daños graves en la finca?", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "¿Cuáles son los riesgos que hace la finca vulnerable?"
        
#Mitigación de riesgos

class PreguntaRiesgo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Riesgo - pregunta"

class Riesgos(models.Model):
    ''' 20 mitigacion de los riesgos
    '''
    pregunta = models.ForeignKey(PreguntaRiesgo, null=True, blank=True)
    respuesta = models.IntegerField('Respuesta', choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Mitigación de los riesgos"
#-------------------------------------------------------------------------------

class TipoCertificacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de certificación"

class Certificacion(models.Model):
    "Tipo de certificación"
    certificacion_finca = models.ManyToManyField(TipoCertificacion, verbose_name="Certificación de la finca",
                                                   null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Certificación de la finca"

