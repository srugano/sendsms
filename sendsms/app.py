#!/usr/bin/env python
# vim : ai ts=4 sts=4 et sw=4
from rapidsms.apps.base import AppBase
from models import Questions, History

class App(AppBase):
        def handle(self, message):
		tel=message.connection.identity
		msg=message.text.lower().split(" ")

		if History.objects.filter(tel_num=tel):				
			"""The phone number is known in our system """
			for q in History.objects.filter(tel_num=tel):	#We pass on each question that we have to ask to the user
				if(q.status==1):
                                        #The question has been asked to the user but the response is not yet registered.So the incoming text message is the response.
					q.reponse=message.text
					q.status=2
					q.save()
				if(q.status==0):
                                        #The question is not yet asked to the user. We have to ask it to him or to her
					q.status=1
					q.save()
					quest=q.question
					message.respond(" %s " %(quest))
					return True
			message.respond("CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !")	#All questions we have prepared to ask to that user for his/her registration have got response
			return True
		elif msg[0]=='joindre':	
			"""The phone number is not known in our system and the user ask for registration"""
			for q in Questions.objects.all():
                                #We put all questions that we will ask to him/her in the table "History"
				h=History(question=q.question,tel_num=tel,status=0)
				h.save()
			if History.objects.filter(tel_num=tel):
                                #The question(s) for registration are available
				message.respond("WELCOME TO RAPIDSMS!")
			else:
				"""The question(s) for registration are not available 
                and the user must try again later to ask for registration 
                """
				message.respond("SORY, TRY AGAIN LATER!")
                        return True
		else:
			"""The phone number is not known in our system and the 
			system must inform to the user the mesage to send if he/she 
			want to be registered """
			message.respond("SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND <JOINDRE> !")
			return True
