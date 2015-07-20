# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Join.zipcode'
        db.add_column(u'register_join', 'zipcode',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True),
                      keep_default=False)

        # Adding field 'Join.area'
        db.add_column(u'register_join', 'area',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Join.ref_id'
        db.add_column(u'register_join', 'ref_id',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=120),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Join.zipcode'
        db.delete_column(u'register_join', 'zipcode')

        # Deleting field 'Join.area'
        db.delete_column(u'register_join', 'area')

        # Deleting field 'Join.ref_id'
        db.delete_column(u'register_join', 'ref_id')


    models = {
        u'register.join': {
            'Meta': {'object_name': 'Join'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'})
        }
    }

    complete_apps = ['register']