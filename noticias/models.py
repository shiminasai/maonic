# -*- coding: UTF-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import utils
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

# crear modelos para las noticias.

class Noticias(models.Model):
    titulo = models.CharField(max_length=200, help_text="Titulo de la noticia")
    slug = models.SlugField(max_length=200, editable=False)
    fecha = models.DateField()
    foto = ImageField(upload_to=utils.get_file_path, blank=True, null=True)
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
        return '/noticias/%s/' % (self.slug)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
