#! /usr/bin/env python
# encoding=utf-8

from django.contrib import admin
from sendsms.models import User, Questions, Responses, States

class UserAdmin(admin.ModelAdmin):
    fields = ['first_name','telephone']
    list_display = ('first_name','telephone')

class QuestionsAdmin(admin.ModelAdmin):
	fields = [ 'question']
	list_display = ('numero','question','release_date')

class ResponsesAdmin(admin.ModelAdmin):
	fields = ['response', 'question']
	list_display = ('response','question','release_date' )

class StatesAdmin(admin.ModelAdmin):
	fields = ['user'  ] 
	list_display = ('user','n_messages')
	
	
admin.site.register(User, UserAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Responses, ResponsesAdmin)
admin.site.register(States, StatesAdmin)
