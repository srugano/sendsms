#!/usr/bin/env python
# vim : ai ts=4 sts=4 et sw=4

import datetime
import time 
from rapidsms.apps.base import AppBase
from sendsms.models import *


class App(AppBase):
	def handle(self, message):
		entry = message.text.split(" ")
		if entry[0] == 'joindre':
			for oui in Questions.objects.all():
				message.respond(oui.question)
				Responses(
				response = str(message.text),
				release_date = datetime.datetime.now(),
				question = oui ).save()
				
				def handle2(self, msg)
					entryB = msg.text.split(" ")
					if entryB[0] == 'oui':
						continue
					else:
						break
		return True
		

		
		
