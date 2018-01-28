from django.shortcuts import render
from first_app.models import Topic, WebPage, AccessRecord
from .forms import FormName
from django.http import HttpResponseRedirect


def index(request):
    topics = Topic.objects.all()
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print('INVALID FORM INPUTS')

    my_dict = {
                'insert_me': topics,
                'form': form,
              }
    return render(request, 'first_app/index.html', context=my_dict)


def form_name_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print('INVALID FORM INPUTS')

    return render(request, 'first_app/form_page.html', {'form': form})
