from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View

from .models import Result

from .pdf import html_to_pdf


def index(request):
    template = 'index.html'
    return render(request, template)


@login_required()
def login(request):
    template = 'longin.html'
    return render(request, template)

@login_required()
def logout(request):
    template = 'registration/login.html'
    return redirect(request, template)


@login_required()
def result_list(request):
    template_name = 'result_list.html'
    objects = Result.objects.filter(active=True, user=request.user)
    context = {'object_list': objects}
    return render(request, template_name, context)


# Creating a class based view
class GeneratePdf(View):
    def get(self, request):
        template_name = 'result_list.html'
        objects = Result.objects.filter(user=request.user)
        context = {'object_list': objects}
        open('temp.html', "w").write(render_to_string(template_name, context))

        # getting the template
        pdf = html_to_pdf('temp.html', context)

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
