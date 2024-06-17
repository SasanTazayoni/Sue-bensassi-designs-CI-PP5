from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """ Renders the home page. """
    
    return render(request, 'core/index.html')


def about(request):
    """ Renders the about page. """
    
    return render(request, 'core/about.html')