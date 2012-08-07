# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Noticias'
        db.create_table('noticias_noticias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagen', self.gf('noticias.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('cuerpo', self.gf('ckeditor.fields.RichTextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, db_index=True)),
        ))
        db.send_create_signal('noticias', ['Noticias'])

        # Adding model 'Adjunto'
        db.create_table('noticias_adjunto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.Noticias'])),
        ))
        db.send_create_signal('noticias', ['Adjunto'])


    def backwards(self, orm):
        
        # Deleting model 'Noticias'
        db.delete_table('noticias_noticias')

        # Deleting model 'Adjunto'
        db.delete_table('noticias_adjunto')


    models = {
        'noticias.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Noticias']"})
        },
        'noticias.noticias': {
            'Meta': {'object_name': 'Noticias'},
            'cuerpo': ('ckeditor.fields.RichTextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('noticias.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['noticias']
