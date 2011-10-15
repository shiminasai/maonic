# -*- coding: UTF-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.

#*** Organizacion gremial ***
#----------------------------

class OrgGremiales(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones Gremiales"

class BeneficiosObtenido(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Benificios Obtenidos"

class SerMiembro(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Porque quiere ser miembro"

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'))
CHOICE_MIEMBRO_GREMIAL = ((1,'Junta directiva'),(2,'Comisiones de trabajo'),(3,'No'))


class OrganizacionGremial(models.Model):
    ''' 2. Organizacion Gremial
    '''
    socio = models.ManyToManyField(OrgGremiales,
                                   verbose_name="Es socio/a de una organización gremial")
    nombre = models.CharField('Nombre de la organización gremial', max_length=200)
    desde_socio = models.IntegerField('Desde cuando', choices=CHOICE_DESDE, null=True, blank=True)
    beneficio = models.ManyToManyField(BeneficiosObtenido,
                                       verbose_name="¿Qué beneficios ha tenido por ser socio/a de la cooperativa, la asociación o empresa", null=True, blank=True)
    miembro_gremial = models.IntegerField('Soy miembro de órgano gremial',
                                          choices=CHOICE_MIEMBRO_GREMIAL, null=True, blank=True)
    desde_miembro = models.IntegerField('Desde cuando', choices=CHOICE_DESDE, null=True, blank=True)
    capacitacion = models.IntegerField('He recibido capacitación para desempeñar mi cargo',
                                      choices=CHOICE_OPCION, null=True, blank=True)
    desde_capacitacion = models.IntegerField('Desde cuando', choices=CHOICE_DESDE, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Organizacion Gremial"
        
#*** Tipo tenencia de parcela y solar ***
#----------------------------------------

CHOICE_TENENCIA = ((1,"Propia con escritura pública"),
                   (2,"Propia por herencia"),
                   (3,"Propias con promesa de venta"),
                   (4,"Propias con titulo de reforma agraria"),
                   (5,"Arrendada"),
                   (6,"Sin documento"),
                   (7,"Escritura posesoria"))
                   
                   
CHOICE_DUENO = ((1,"Hombre"),
                (2,"Mujer"),
                (3,"Mancomunado"),
                (4,"Parientes"),
                (5,"Colectivo"),
                (6,"No hay"))

class Tenencia(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.IntegerField('Tipo de tenencia Parcela', choices=CHOICE_TENENCIA, null=True, blank=True)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_parcela_display()
        
    class Meta:
        verbose_name_plural = "Tipos de tenencia de la parcela y el solar"      
        
