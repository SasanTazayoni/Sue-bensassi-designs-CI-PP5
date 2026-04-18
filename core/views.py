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


def terms(request):
    """ Renders the terms & conditions page. """

    return render(request, 'core/terms.html')


def cookie_policy(request):
    """ Renders the cookie policy page. """

    return render(request, 'core/cookie_policy.html')


def privacy_policy(request):
    """ Renders the privacy policy page. """

    return render(request, 'core/privacy_policy.html')
