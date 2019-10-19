from django.shortcuts import render
from django.http import HttpResponse
from models import Applications

# Create your views here.
def detail(request, app_pkg):
    return HttpResponse("You're looking at question : %s" %(app_pkg))


def index(request):
    latest_question_list = Applications.objects.order_by('-careted_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return "Dashboard"