from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
        else:
            messages.error(
                request,
                f'There was an error with the form. Please check the'
                f'information provided.'
            )
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    enquiries = profile.enquiries.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'enquiries': enquiries,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Generate order history. """

    order = get_object_or_404(Order, order_number=order_number)

    messages.warning(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
