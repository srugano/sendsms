#!/usr/bin/env python
# vim : ai ts=4 sts=4 et sw=4

from rapidsms.apps.base import AppBase
from pingpong.models import *
import datetime
class App(AppBase):
    def handle(self, message):
        num_tel = message.peer
        entry = message.text.lower().split(" ")
        now = datetime.datetime.now()
        #ordre = [ int(x) for x in Ordre.objects.get(pk=1) ]
        i = 0
        if entry[0] == 'joindre':
            message.respond("thank you for joining ")

        try :
            if States.objects.filter(num_tel__exat=int(num_tel)):
                i = States.objects.filter(num_tel=int(num_tel)).n_messages
                ni = i+1
                States.objects.get(num_tel=int(num_tel), n_messages=ni).save(update_fields=True)
                Responses(
                    response=message.text,
                    release_date=now,
                    question=Questions.objects.get(pk=n+i)
                    ).save()
                return True
        except LookupError:
            message.respond("You're not registered")

        if States.objects.filter(num_tel__exat=int(num_tel)) == False :
            States(
                num_tel=int(message.peer),
                n_messages=0
                ).save()
            Responses(
                response=message.text,
                release_date=now,
                question=Questions.objects.get(pk=1)
                ).save()
            return True
        nm = States.objects.filter(num_tel__exat=int(num_tel)).n_messages
        message.respond("Thanks. %s " % Questions.objects.get(pk=nm).question)
        return True
