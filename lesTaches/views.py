from django.shortcuts import render
from django.http import HttpResponse
from lesTaches.models import Task

def home(request, param):
    return HttpResponse('bonjour à tous ' + param)

def task_listing(request):
    from django.template import Template, Context
    objets = Task.objects.all().order_by('due_date')
    return render(request,'lesTaches/list.html',{'objets':objets})
