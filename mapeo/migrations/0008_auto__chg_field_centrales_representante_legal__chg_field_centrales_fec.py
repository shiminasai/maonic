# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Centrales.representante_legal'
        db.alter_column('mapeo_centrales', 'representante_legal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Centrales.fecha_est'
        db.alter_column('mapeo_centrales', 'fecha_est', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Centrales.num_hombres'
        db.alter_column('mapeo_centrales', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Centrales.direccion'
        db.alter_column('mapeo_centrales', 'direccion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Centrales.num_mujeres'
        db.alter_column('mapeo_centrales', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Centrales.tipo_org'
        db.alter_column('mapeo_centrales', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.TipoOrganizacion'], null=True))

        # Changing field 'Centrales.representante_tecnico'
        db.alter_column('mapeo_centrales', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Uniones.representante_legal'
        db.alter_column('mapeo_uniones', 'representante_legal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Uniones.fecha_est'
        db.alter_column('mapeo_uniones', 'fecha_est', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Uniones.num_hombres'
        db.alter_column('mapeo_uniones', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Uniones.direccion'
        db.alter_column('mapeo_uniones', 'direccion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Uniones.num_mujeres'
        db.alter_column('mapeo_uniones', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Uniones.tipo_org'
        db.alter_column('mapeo_uniones', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.TipoOrganizacion'], null=True))

        # Changing field 'Uniones.representante_tecnico'
        db.alter_column('mapeo_uniones', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AsistenciaTecnica.nombre_org'
        db.alter_column('mapeo_asistenciatecnica', 'nombre_org_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['mapeo.Cooperativa'], null=True))

        # Changing field 'Asociacion.representante_legal'
        db.alter_column('mapeo_asociacion', 'representante_legal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Asociacion.fecha_est'
        db.alter_column('mapeo_asociacion', 'fecha_est', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Asociacion.central'
        db.alter_column('mapeo_asociacion', 'central_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Centrales'], null=True))

        # Changing field 'Asociacion.num_hombres'
        db.alter_column('mapeo_asociacion', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Asociacion.direccion'
        db.alter_column('mapeo_asociacion', 'direccion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Asociacion.num_mujeres'
        db.alter_column('mapeo_asociacion', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Asociacion.tipo_org'
        db.alter_column('mapeo_asociacion', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.TipoOrganizacion'], null=True))

        # Changing field 'Asociacion.representante_tecnico'
        db.alter_column('mapeo_asociacion', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Cooperativa.representante_legal'
        db.alter_column('mapeo_cooperativa', 'representante_legal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Cooperativa.fecha_est'
        db.alter_column('mapeo_cooperativa', 'fecha_est', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Cooperativa.num_hombres'
        db.alter_column('mapeo_cooperativa', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Cooperativa.direccion'
        db.alter_column('mapeo_cooperativa', 'direccion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Cooperativa.num_mujeres'
        db.alter_column('mapeo_cooperativa', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Cooperativa.tipo_org'
        db.alter_column('mapeo_cooperativa', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.TipoOrganizacion'], null=True))

        # Changing field 'Cooperativa.representante_tecnico'
        db.alter_column('mapeo_cooperativa', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'Centrales.representante_legal'
        db.alter_column('mapeo_centrales', 'representante_legal', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Centrales.fecha_est'
        db.alter_column('mapeo_centrales', 'fecha_est', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Centrales.num_hombres'
        db.alter_column('mapeo_centrales', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Centrales.direccion'
        db.alter_column('mapeo_centrales', 'direccion', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Centrales.num_mujeres'
        db.alter_column('mapeo_centrales', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Centrales.tipo_org'
        db.alter_column('mapeo_centrales', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['mapeo.TipoOrganizacion']))

        # Changing field 'Centrales.representante_tecnico'
        db.alter_column('mapeo_centrales', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Uniones.representante_legal'
        db.alter_column('mapeo_uniones', 'representante_legal', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Uniones.fecha_est'
        db.alter_column('mapeo_uniones', 'fecha_est', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Uniones.num_hombres'
        db.alter_column('mapeo_uniones', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Uniones.direccion'
        db.alter_column('mapeo_uniones', 'direccion', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Uniones.num_mujeres'
        db.alter_column('mapeo_uniones', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Uniones.tipo_org'
        db.alter_column('mapeo_uniones', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['mapeo.TipoOrganizacion']))

        # Changing field 'Uniones.representante_tecnico'
        db.alter_column('mapeo_uniones', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'AsistenciaTecnica.nombre_org'
        db.alter_column('mapeo_asistenciatecnica', 'nombre_org_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(default='', to=orm['mapeo.Cooperativa']))

        # Changing field 'Asociacion.representante_legal'
        db.alter_column('mapeo_asociacion', 'representante_legal', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Asociacion.fecha_est'
        db.alter_column('mapeo_asociacion', 'fecha_est', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Asociacion.central'
        db.alter_column('mapeo_asociacion', 'central_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['mapeo.Centrales']))

        # Changing field 'Asociacion.num_hombres'
        db.alter_column('mapeo_asociacion', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Asociacion.direccion'
        db.alter_column('mapeo_asociacion', 'direccion', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Asociacion.num_mujeres'
        db.alter_column('mapeo_asociacion', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Asociacion.tipo_org'
        db.alter_column('mapeo_asociacion', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['mapeo.TipoOrganizacion']))

        # Changing field 'Asociacion.representante_tecnico'
        db.alter_column('mapeo_asociacion', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Cooperativa.representante_legal'
        db.alter_column('mapeo_cooperativa', 'representante_legal', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Cooperativa.fecha_est'
        db.alter_column('mapeo_cooperativa', 'fecha_est', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Cooperativa.num_hombres'
        db.alter_column('mapeo_cooperativa', 'num_hombres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Cooperativa.direccion'
        db.alter_column('mapeo_cooperativa', 'direccion', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Cooperativa.num_mujeres'
        db.alter_column('mapeo_cooperativa', 'num_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Cooperativa.tipo_org'
        db.alter_column('mapeo_cooperativa', 'tipo_org_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['mapeo.TipoOrganizacion']))

        # Changing field 'Cooperativa.representante_tecnico'
        db.alter_column('mapeo_cooperativa', 'representante_tecnico', self.gf('django.db.models.fields.CharField')(default='', max_length=100))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'mapeo.areatrabajo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'AreaTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.asistenciatecnica': {
            'Meta': {'object_name': 'AsistenciaTecnica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': "'8'", 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_org': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['mapeo.Cooperativa']", 'null': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': "'8'", 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.TipoOrganizacion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.asociacion': {
            'Meta': {'object_name': 'Asociacion'},
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'central': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.Centrales']", 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rubros': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Rubros']", 'symmetrical': 'False', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.TipoOrganizacion']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.buenaspracticas': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'BuenasPracticas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.centrales': {
            'Meta': {'object_name': 'Centrales'},
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_asociaciones': ('django.db.models.fields.IntegerField', [], {}),
            'num_cooperativas': ('django.db.models.fields.IntegerField', [], {}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rubros': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Rubros']", 'symmetrical': 'False', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.TipoOrganizacion']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.certificacion': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Certificacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.certificadora': {
            'Meta': {'object_name': 'Certificadora'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.cominsumo': {
            'Meta': {'object_name': 'ComInsumo'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde_insumo': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.comproducto': {
            'Meta': {'object_name': 'ComProducto'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_prov': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.cooperativa': {
            'Meta': {'object_name': 'Cooperativa'},
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'central': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.Centrales']", 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rubros': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Rubros']", 'symmetrical': 'False', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.TipoOrganizacion']", 'null': 'True', 'blank': 'True'}),
            'union': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.Uniones']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.familia': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Familia'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'area_finca': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'asociacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.Asociacion']", 'null': 'True', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': "'8'", 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cooperativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.Cooperativa']", 'null': 'True', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_finca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': "'8'", 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.TipoOrganizacion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.financiera': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Financiera'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.materiaprocesada': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'MateriaProcesada'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.orgpublica': {
            'Meta': {'object_name': 'OrgPublica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.rubroanimales': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'RubroAnimales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubroarboles': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'RubroArboles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubrocultivo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'RubroCultivo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubros': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Rubros'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.semilla': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Semilla'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.tipoorganizacion': {
            'Meta': {'object_name': 'TipoOrganizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.uniones': {
            'Meta': {'object_name': 'Uniones'},
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_cooperativas': ('django.db.models.fields.IntegerField', [], {}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rubros': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Rubros']", 'symmetrical': 'False', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapeo.TipoOrganizacion']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['mapeo']
