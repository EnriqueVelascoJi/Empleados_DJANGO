from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def second_view(request):
    
    frutas = ['apple', 'pineapple', 'cucumber', 'strawberry']
    return render (request, 'template_test.html', {
        'fruits': frutas
    })
