# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ordre'
        db.create_table(u'pingpong_ordre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordre', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('num_poll', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'pingpong', ['Ordre'])

        # Deleting field 'States.ordre'
        db.delete_column(u'pingpong_states', 'ordre')

        # Deleting field 'States.user'
        db.delete_column(u'pingpong_states', 'user_id')

        # Adding field 'States.num_tel'
        db.add_column(u'pingpong_states', 'num_tel',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Ordre'
        db.delete_table(u'pingpong_ordre')

        # Adding field 'States.ordre'
        db.add_column(u'pingpong_states', 'ordre',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'States.user'
        raise RuntimeError("Cannot reverse this migration. 'States.user' and its values cannot be restored.")
        # Deleting field 'States.num_tel'
        db.delete_column(u'pingpong_states', 'num_tel')


    models = {
        u'pingpong.ordre': {
            'Meta': {'ordering': "('num_poll',)", 'object_name': 'Ordre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_poll': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'ordre': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'pingpong.questions': {
            'Meta': {'ordering': "('release_date',)", 'object_name': 'Questions'},
            'numero': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'})
        },
        u'pingpong.responses': {
            'Meta': {'ordering': "('release_date',)", 'object_name': 'Responses'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pingpong.Questions']"}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'pingpong.states': {
            'Meta': {'ordering': "('num_tel',)", 'object_name': 'States'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n_messages': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'num_tel': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'pingpong.user': {
            'Meta': {'ordering': "('first_name',)", 'object_name': 'User'},
            'answear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.IntegerField', [], {'default': '123456'})
        }
    }

    complete_apps = ['pingpong']