from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from .models import NewsletterSubscription
from .forms import NewsletterForm


@require_POST
def newsletter_subscribe(request):
    """ 
    A view to handle new sign ups to the newsletter mailing list.
    """

    email = request.POST.get("email")
    if not email:
        messages.warning(
            request, 'An email address is required to subscribe.'
        )
        return redirect(reverse('home'))

    if not NewsletterSubscription.objects.filter(email=email).exists():
        NewsletterSubscription.objects.create(email=email)
        messages.success(
            request, 'You have subscribed to our mailing list.'
        )

    else:
        messages.warning(
            request, 'This email is already subscribed.'
        )

    return redirect(reverse('home'))
