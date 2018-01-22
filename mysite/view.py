import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from mysite.models import Question
from mysite.settings import BASE_DIR

def getQuestion(id):
    return Question.objects.get(id=id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % getQuestion(question_id))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mysite/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
