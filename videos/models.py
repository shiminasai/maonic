from django.db import models

# Create your models here.

class Video(models.Model):
	nombre = models.CharField(max_length=200)
	url = models.URLField()

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name=u'Video'
		verbose_name_plural = u'Videos'


