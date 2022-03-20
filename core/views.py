from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .models import Result

# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)

@login_required()
def login(request):
    template = 'longin.html'
    return render(request, template)


def logout(request):
    template = 'registration/login.html'
    return redirect(request, template)


@login_required()
def result_list(request):
    template_name = 'result_list.html'
    objects = Result.objects.filter(active=True, user=request.user)
    context = {'object_list': objects}
    return render(request, template_name, context)

