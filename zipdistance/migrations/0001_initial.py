# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ZipDistance'
        db.create_table(u'zipdistance_zipdistance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'zipdistance', ['ZipDistance'])


    def backwards(self, orm):
        # Deleting model 'ZipDistance'
        db.delete_table(u'zipdistance_zipdistance')


    models = {
        u'zipdistance.zipdistance': {
            'Meta': {'ordering': "['zipcode']", 'object_name': 'ZipDistance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'})
        }
    }

    complete_apps = ['zipdistance']