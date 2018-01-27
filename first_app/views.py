from django.shortcuts import render
from first_app.models import Topic, WebPage, AccessRecord
from . import forms
from .user_form import UserForm


def index(request):
    date_access = AccessRecord.objects.order_by('date')
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation Success!')
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("ABOUT ME: " + form.cleaned_data['about_me'])
    my_dict = {
                'insert_me': date_access,
                'form': form
              }
    return render(request, 'first_app/index.html', context=my_dict)


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation Success!')
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("ABOUT ME: " + form.cleaned_data['about_me'])
    return render(request, 'first_app/form_page.html', {'form': form})


def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("INVALID FORM")
    return render(request, "first_app/users.html", {'form': form})
