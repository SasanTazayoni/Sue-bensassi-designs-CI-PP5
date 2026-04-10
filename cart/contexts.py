from products.models import Product


def cart_contents(request):

    cart_items = []
    grand_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    product_map = {
        str(p.pk): p
        for p in Product.objects.filter(pk__in=cart.keys())
    }

    for item_id, quantity in cart.items():
        product = product_map.get(item_id)
        if not product:
            continue
        grand_total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
