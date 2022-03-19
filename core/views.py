from django.shortcuts import render

# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)


def login(request):
    template = 'longin.html'
    return render(request, template)

