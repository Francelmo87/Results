from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ResultForm

from .models import Result

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


# listar fornecedores Com CBV
class ResultList(ListView):
    login_url = '/login/'
    model = Result
    template_name = 'result_list.html'