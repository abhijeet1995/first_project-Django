from django.shortcuts import render
from first_app.models import Topic, WebPage, AccessRecord


def index(request):
    date_access = AccessRecord.objects.order_by('date')
    my_dict = {'insert_me': date_access}
    return render(request, 'first_app/index.html', context=my_dict)
