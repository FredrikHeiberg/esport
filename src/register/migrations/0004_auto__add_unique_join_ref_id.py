# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Join', fields ['ref_id']
        db.create_unique(u'register_join', ['ref_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Join', fields ['ref_id']
        db.delete_unique(u'register_join', ['ref_id'])


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
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'default'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'})
        }
    }

    complete_apps = ['register']