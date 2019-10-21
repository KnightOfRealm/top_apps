from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from models import Applications

# Create your views here.
def detail(request):
    pkg = request.GET.get('pkg')
    app = Applications.objects.filter(package=pkg)
    if app.exists():
        return HttpResponse("FOUND : %s" %(app[0].__dict__))
    return HttpResponse("Please check the package name : %s" %(request.GET.get('pkg')))


def index(request):
    apps = Applications.objects.order_by('-created_date')
    template = loader.get_template('apps/index.html')
    context = {
        'apps': apps,
    }
    return HttpResponse(template.render(context, request))