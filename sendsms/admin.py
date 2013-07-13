#! /usr/bin/env python
# encoding=utf-8
from django.contrib import admin
from sendsms.models import Questions

class QuestionsAdmin(admin.ModelAdmin):
    #fields = ['question', 'reponse']
    fields = ['question']

admin.site.register(Questions, QuestionsAdmin)
