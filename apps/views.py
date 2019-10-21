from django.shortcuts import render
from django.http import HttpResponse
from models import Applications

# Create your views here.
def detail(request):
    pkg = request.GET.get('pkg')
    app = Applications.objects.filter(package=pkg)
    if app.exists():
        return HttpResponse("FOUND : %s" %(app[0].__dict__))
    return HttpResponse("Please check the package name : %s" %(request.GET.get('pkg')))


def index(request):
    latest_question_list = Applications.objects.order_by('-careted_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return "Dashboard"