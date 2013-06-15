#! /usr/bin/env python
# encoding=utf-8

from django.contrib import admin
from pingpong.models import User, Questions, Responses, States, Ordre

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
	fields = ['num_tel', 'n_messages',  ] 
	list_display = ('num_tel','n_messages')

class OrdreAdmin(admin.ModelAdmin):
	fields = ['ordre', 'num_poll',  ] 
	list_display = ('ordre','num_poll')	
	
admin.site.register(User, UserAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Responses, ResponsesAdmin)
admin.site.register(States, StatesAdmin)
admin.site.register(Ordre, OrdreAdmin)
