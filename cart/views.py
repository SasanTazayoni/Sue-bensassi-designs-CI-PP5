from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages
from products.models import Product
from urllib.parse import urlencode


def view_cart(request):
    """ A view that renders the contents of the cart. """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart. """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') or reverse('products')

    cart = request.session.get('cart', {})

    if item_id in cart:
        if product.stock >= cart[item_id] + quantity:
            cart[item_id] += quantity
            messages.info(request, f'{quantity} {product.name} added to \
                your cart.')
        else:
            messages.error(
                request, f'Error: {product.name} has only {product.stock} \
                    units left. You currently have {cart[item_id]} in \
                    your cart.'
            )
    else:
        cart[item_id] = quantity
        messages.info(request, f'{quantity} {product.name} added to \
            your cart.')

    request.session['cart'] = cart

    # Construct the redirect URL with preserved query parameters
    if request.GET:
        redirect_url += '?' + urlencode(request.GET)

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if quantity <= product.stock:
            cart[item_id] = quantity
            messages.info(
                request, f'{product.name} quantity updated to {quantity}.'
            )
        else:
            messages.error(
                request, f'Error: {product.name} has only \
                    {product.stock} units left.'
            )
    else:
        messages.error(request, 'Quantity must be greater than zero.')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the specified product from the cart. """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        if item_id in cart:
            del cart[item_id]
            messages.info(request, f'{product.name} removed from your cart.')
        else:
            messages.error(request, f'{product.name} is not in your cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
