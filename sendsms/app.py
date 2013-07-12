#!/usr/bin/env python
# vim : ai ts=4 sts=4 et sw=4
from rapidsms.apps.base import AppBase
from sendsms.models import Questions, History

class App(AppBase):
	def handle(self, message):
		tel=message.connection.identity
		msg=message.text.lower().split(" ")
		if msg[0]=='joindre':
			for q in Questions.objects.all():
				h=History(question=q.question,tel_num=tel,status=0)
				h.save()
			message.respond("WELCOME TO RAPIDSMS")
			return True
		elif History.objects.filter(tel_num=tel):
			for q in (History.objects.filter(tel_num=tel)):
				if(q.status==1):
					q.reponse=message.text
					q.status=2
					q.save()
				if(q.status==0):
					q.status=1
					q.save()
					quest=q.question
					message.respond(" %s " %(quest))
					return True
			message.respond("CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !")
			return True
		else:
			message.respond("SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND JO !")
			return True
		
		
