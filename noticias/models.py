# -*- coding: UTF-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from maonic.utils import get_file_path
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from image_cropping import ImageRatioField

# crear modelos para las noticias.

class Noticias(models.Model):
    titulo = models.CharField(max_length=200, help_text="Titulo de la noticia")
    slug = models.SlugField(max_length=200, editable=False)
    fecha = models.DateField()
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)
    contenido = RichTextField()
    destacado = models.BooleanField()
    

    fileDir = 'noticias/'

    autor = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Noticias, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/noticias/detalles/%s/' % (self.slug)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

class Portada(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    def _fotos_traer(self):
        todas = FotosPortadas.objects.filter(portada__id=self.id)
        return todas

class FotosPortadas(models.Model):
    portada = models.ForeignKey(Portada)
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    cropping = ImageRatioField('foto', '1500x480')

    fileDir = 'fotoPortadas/'

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Fotos portadas'