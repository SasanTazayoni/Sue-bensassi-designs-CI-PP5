from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount. """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if quantity <= product.stock:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} quantity updated to {quantity}.')
        else:
            messages.error(request, f'Error: {product.name} has only {product.stock} units left.')
    else:
        if item_id in cart:
            del cart[item_id]
            messages.success(request, f'{product.name} removed from your cart.')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))