#!/usr/bin/env python
# vim : ai ts=4 sts=4 et sw=4

from rapidsms.apps.base import AppBase
from sendsms.models import *
from django.core.exceptions import ObjectDoesNotExist
import datetime

class App(AppBase):
    def handle(self, message):
        num_tel = message.connection.identity                    	 	# phone number of the sender
        entry = message.text.lower().split(" ")                 	 	# fetch the sent text
        now = datetime.datetime.now()
        #ordre = [ int(x) for x in Ordre.objects.get(pk=1) ]
        i = 0

        try :
            i = States.objects.get(num_tel=int(num_tel)).n_messages 	# in case the sender is allready registered, this will work 'i' can't be == 0
            ni = i+1
            e = States.objects.get(num_tel__exact=int(num_tel))
            e.n_messages = ni
            e.save() # update the number of messages actaly sent by the user
            Responses.objects.create(
                response=message.text,
                release_date=now,
                question=Questions.objects.get(pk=i)
                ) # store the response
            ha = int(num_tel)
            y = States.objects.get(num_tel__exact=ha).n_messages
            message.respond("Thanks. %s " % Questions.objects.get(pk=y).question) # ask the next question
            return True

        except ObjectDoesNotExist:
            if entry[0] == 'joindre' :
                States.objects.create(
                    num_tel=num_tel,
                    n_messages=1
                    )
		message.respond("thank you for joining. %s " % Questions.objects.get(pk=1).question) # ask the next question
		return True
	    else :
                message.respond("You're not regitered. For joining, just send 'joindre' ")
                return True
