#! /usr/bin/env python
# encoding=utf-8
from django.contrib import admin
<<<<<<< HEAD
from sendsms.models import User, Questions, Responses, States
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name','telephone']
    list_display = ('first_name','telephone')
=======
from sendsms.models import Questions

>>>>>>> 6973353f84d6d8c9c369d61ec66714fb478b4e90

class QuestionsAdmin(admin.ModelAdmin):
    #fields = ['question', 'reponse']
    fields = ['question']

<<<<<<< HEAD
class StatesAdmin(admin.ModelAdmin):
	fields = ['num_tel' ] 
	list_display = ('num_tel',)

"""class OrdreAdmin(admin.ModelAdmin):
	fields = ['ordre', 'num_poll',  ] 
	list_display = ('ordre','num_poll')	
"""
admin.site.register(User, UserAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Responses, ResponsesAdmin)
admin.site.register(States, StatesAdmin)
"""admin.site.register(Ordre, OrdreAdmin) """
=======
admin.site.register(Questions, QuestionsAdmin)
>>>>>>> 6973353f84d6d8c9c369d61ec66714fb478b4e90
