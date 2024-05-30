from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(
            request,
            "There is nothing in your shopping cart at the moment."
        )
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P3hP7KwtsxyNH1WcpnUD44uBMEiX6XEtEvbYYALDn34yG4hqPioK6xHGQ49fUrEfFxonYBhVtQJuh0kANnFenqS00rhR6LczN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
