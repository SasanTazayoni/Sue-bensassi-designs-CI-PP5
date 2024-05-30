from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view that renders the contents of the cart. """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart. """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if product.stock >= cart[item_id] + quantity:
            cart[item_id] += quantity
        else:
            messages.error(
                request, f'Error {product.name} has only {product.stock} units \
                    left, you currently have {cart[item_id]} in your cart.'
            )

    request.session['cart'] = cart
    return redirect(redirect_url)
