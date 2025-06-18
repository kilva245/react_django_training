from django.shortcuts import render
from . import models

def homepage(request):
    return render(request=request, template_name='home.html')

def temp(request):
    name = models.Person.objects.all()
    
    context = {
        'peaple' : name,
    }
    return render(request=request, template_name='temp.html', context=context)