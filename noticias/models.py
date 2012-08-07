# -*- coding: UTF-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from noticias.thumbs import ImageWithThumbsField
from ckeditor.fields import RichTextField
import utils

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^noticias\.thumbs\.ImageWithThumbsField"])

# crear modelos para las noticias.

class Noticias(models.Model):
    titulo = models.CharField(max_length=200, help_text="Titulo de la noticia") #noticia
    imagen = ImageWithThumbsField(upload_to=utils.get_file_path, sizes=((96, 128), (194, 124), (360, 215), (570, 272)), blank=True, null=True)   
    fecha = models.DateField()
    cuerpo = RichTextField()                #texto
    slug = models.SlugField(max_length=200, editable=False)
    

    fileDir = 'noticias/'

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kargs):
        if not self.id:
                n = Noticias.objects.all().count()
                self.slug = '%s-%s'[:200] % (n, slugify(self.titulo))
        super(Noticias, self).save(*args, **kargs)

    @models.permalink
    def get_absolute_url(self):
        return ('moanic', [self.slug])

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

class Adjunto(models.Model):
    nombre = models.CharField(max_length=200)
    adjunto = models.FileField(upload_to=utils.get_file_path)
    noticia = models.ForeignKey(Noticias)

    fileDir = 'adjuntos_noticias/'

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Adjuntar"