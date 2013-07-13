<<<<<<< HEAD
from rapidsms.apps.base import AppBase
from sendsms.models import Questions, Responses, States
from fonctions import enregistre, initialise
class App(AppBase):
    def handle(self, message):
        tel=message.connection.identity
        msg=message.text.split(" ")
        if msg[0]=='joindre':
			initialise(tel)
			message.respond("WELCOME TO RAPIDSMS")
			return True
        elif States.objects.filter(num_tel=tel):
            enregistre(message.text)
            message.respond("CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !")
            return True
        else :
            message.respond("You're not registered. Send 'joindre'")
            return True
=======
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
		
		
>>>>>>> 6973353f84d6d8c9c369d61ec66714fb478b4e90
