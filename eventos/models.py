from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import utils
from sorl.thumbnail import ImageField

# Create your models here.

class Evento(models.Model):
	titulo = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, editable=False)
	foto = ImageField(upload_to=utils.get_file_path, blank=True, null=True)
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	descripcion = RichTextField()
	ubicacion = models.CharField(max_length=200)

	fileDir = 'eventos/'

	autor = models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = (slugify(self.titulo))
		super(Evento, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/eventos/%s/' % (self.slug)

	class Meta:
		verbose_name=u'Evento'
		verbose_name_plural = 'Eventos'

