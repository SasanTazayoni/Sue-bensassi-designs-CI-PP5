from django.shortcuts import render


def home(request):
    """ Renders the home page. """

    return render(request, 'core/index.html')


def about(request):
    """ Renders the about page. """

    return render(request, 'core/about.html')

def delivery(request):
    """ Renders the delivery page. """

    return render(request, 'core/delivery.html')
