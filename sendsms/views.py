from django.shortcuts import render,  get_object_or_404

from sendsms.models import Questions, History


def index(request):
    questions_list = Questions.objects.all().order_by('Questions')[:5]
    context = {'questions_list': user_list}
    return render(request, 'sendsms/index.html', context)

def detail(request, poll_id):
    questions = get_object_or_404(Questions, pk=user_id)
    return render(request, 'sendsms/detail.html', {'user': questions})
