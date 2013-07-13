# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'sendsms_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answear', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('telephone', self.gf('django.db.models.fields.IntegerField')(default=123456)),
        ))
        db.send_create_signal(u'sendsms', ['User'])

        # Adding model 'Questions'
        db.create_table(u'sendsms_questions', (
            ('numero', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('release_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 6, 21, 0, 0))),
        ))
        db.send_create_signal(u'sendsms', ['Questions'])

        # Adding model 'Responses'
        db.create_table(u'sendsms_responses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('release_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 6, 21, 0, 0))),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sendsms.Questions'])),
            ('user', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'sendsms', ['Responses'])

        # Adding model 'States'
        db.create_table(u'sendsms_states', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_tel', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sendsms.Questions'])),
        ))
        db.send_create_signal(u'sendsms', ['States'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'sendsms_user')

        # Deleting model 'Questions'
        db.delete_table(u'sendsms_questions')

        # Deleting model 'Responses'
        db.delete_table(u'sendsms_responses')

        # Deleting model 'States'
        db.delete_table(u'sendsms_states')


    models = {
        u'sendsms.questions': {
            'Meta': {'ordering': "('release_date',)", 'object_name': 'Questions'},
            'numero': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 6, 21, 0, 0)'})
        },
        u'sendsms.responses': {
            'Meta': {'ordering': "('release_date', 'question')", 'object_name': 'Responses'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sendsms.Questions']"}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 6, 21, 0, 0)'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'sendsms.states': {
            'Meta': {'ordering': "('num_tel',)", 'object_name': 'States'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_tel': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sendsms.Questions']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'sendsms.user': {
            'Meta': {'ordering': "('first_name',)", 'object_name': 'User'},
            'answear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.IntegerField', [], {'default': '123456'})
        }
    }

    complete_apps = ['sendsms']