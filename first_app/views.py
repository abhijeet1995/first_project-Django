from django.shortcuts import render


def index(request):
    my_dict = {'insert_me': "Hello, I'm from first app"}
    return render(request, 'first_app/index.html', context=my_dict)
