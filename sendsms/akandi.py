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
                    enregistre(message.text, tel)
                    message.respond("CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !")
			return True
                else :
                    message.respond("You're not registered. Send 'joindre'")
                    return True
