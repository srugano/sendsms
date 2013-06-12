from django.shortcuts import render,  get_object_or_404

from sendsms.models import User


def index(request):
    user_list = User.objects.all().order_by('first_name')[:5]
    context = {'user_list': user_list}
    return render(request, 'sendsms/index.html', context)

def detail(request, poll_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'sendsms/detail.html', {'user': user})
