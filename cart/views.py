from django.shortcuts import render


def view_cart(request):
    """ A view that renders the contents of the cart. """

    return render(request, 'cart/cart.html')
