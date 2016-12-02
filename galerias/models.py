# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from maonic.utils import get_file_path
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Galeria(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    descripcion = models.TextField()

    autor = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Galeria, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'


class FotoGalerias(models.Model):
    galeria = models.ForeignKey(Galeria)
    titulo = models.CharField(max_length=250)
    foto = ImageField(upload_to=get_file_path)

    fileDir = 'galerias/'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Foto de la galeria'
        verbose_name_plural = 'Fotos de las galerias'