from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
import utils
from django.template.defaultfilters import slugify
from tagging_autocomplete.models import TagAutocompleteField
from tagging.fields import TagField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["tagging_autocomplete\.models\.TagAutocompleteField"])

# Create your models here.


class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, editable=False)
	fecha = models.DateField()
	foto = ImageField(upload_to=utils.get_file_path, blank=True, null=True)
	archivo = models.FileField(upload_to=utils.get_file_path, blank=True, null=True)
	categoria= TagField(help_text='Separar elementos con "," ', 
                                    null=True, blank=True)
	fileDir = 'publicaciones/'

	autor = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = (slugify(self.titulo))
		super(Publicacion, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/publicaciones/%s/' % (self.slug)

	class Meta:
		verbose_name = "Publicacion"
		verbose_name_plural = "Publicaciones"
