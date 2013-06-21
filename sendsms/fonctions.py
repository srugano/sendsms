from sendsms.models import Questions, Responses, States

def initialise(num):
    for q in Questions.objects.all():
        States.objects.create(
            question=q.question,
            tel_num=num,
            status=0
            )

def enregistre(text, tel):
    for q in States.objects.get(tel_num=tel):
        if(q.status==1):
            Responses.objects.create(
                response=        text,
                release_date=now,
                question=Questions.objects.get(pk=i)
                )
            q.reponse=message.text
            q.status=2
            q.save()
        if(q.status==0):
            q.status=1
            q.save()
            quest=q.question
            message.respond(" %s " %(quest))
