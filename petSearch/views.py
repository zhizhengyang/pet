from __future__ import absolute_import, division, print_function
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from django_mongoengine import views
from django.template import loader

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def result(request):
    web_list = ['http://www.baidu.com','http://www.google.com','http://www.alibaba.com']
    template = loader.get_template('result.html')
    context = {
        'web_list': web_list,
    }
    return render(request,'result.html',context)

def index(request):
    context = {}
    return render(request,'index.html',context)

# Create your views here.
