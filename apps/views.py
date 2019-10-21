from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from scrapy.scraper import Scrapy
from models import Applications

def getData():
    scrapy = Scrapy()
    scrapy.getData()


def detail(request):
    pkg = request.GET.get('pkg')
    app = Applications.objects.filter(package=pkg)
    if app.exists():
        template = loader.get_template('apps/details.html')
        context = {
            'app': app[0],
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Please check the package name : %s" %(request.GET.get('pkg')))


def index(request):
    getData()
    apps = Applications.objects.order_by('-created_date')
    template = loader.get_template('apps/index.html')
    context = {
        'apps': apps,
    }
    return HttpResponse(template.render(context, request))

