from django.shortcuts import render
from .models import *


def trees(request):
    context = {
        'genres': Genre.objects.all()
    }
    return render(request, 'trees/test.html', context=context)

def get_elements(request):
    pass