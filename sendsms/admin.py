#! /usr/bin/env python
# encoding=utf-8
from django.contrib import admin
from sendsms.models import Questions, History

class QuestionsAdmin(admin.ModelAdmin):
    fields = ['question']
    list_display = ('question',)

class HistoryAdmin(admin.ModelAdmin):
    fields = ['tel_num', 'response', 'question', 'status']
    list_display = ('response','question',)

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(History, HistoryAdmin)
