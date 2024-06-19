from django.shortcuts import render
from random import choice
from products.models import FakeItem


def handler404(request, exception):
    """ Custom view to handle 404 errors. """

    random_fake_item = FakeItem.objects.order_by('?').first()
    context = {
        'random_fake_item': random_fake_item,
    }
    return render(request, '404.html', context=context)


def handler500(request):
    """ Error Handler 500 - Internal server error. """

    return render(request, "errors/500.html", status=500)
