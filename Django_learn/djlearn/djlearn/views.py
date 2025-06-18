from django.shortcuts import render

def homepage(request):
    return render(request=request, template_name='home.html')

def temp(request):
    context = {
        'key' : 'value',
        'name' : 'John',
        'person' : {
            'name' : 'John',
            'age' : '26'
        }
    }
    return render(request=request, template_name='temp.html', context=context)