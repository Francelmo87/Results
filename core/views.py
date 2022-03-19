from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)


def login(request):
    template = 'longin.html'
    return render(request, template)


def logout(request):
    template = 'registration/login.html'
    return redirect(request, template)
