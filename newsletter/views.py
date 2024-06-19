from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from .models import NewsletterSubscription
# from .forms import NewsletterForm


@require_POST
def newsletter_subscribe(request):
    """ 
    A view to handle new sign ups to the newsletter mailing list.
    """

    email = request.POST.get("email")
    # is email provided?
    if not email:
        return JsonResponse({
            "success": False,
            "message": "A valid Email is required."
        })

    if not NewsletterSubscription.objects.filter(email=email).exists():
        # email not already subscribed > proceed
        NewsletterSubscription.objects.create(email=email)
        return JsonResponse({
            "success": True,
            "message": "Thank you for subscribing!",
        })

    else:
        # found existing email subscribed > stop
        return JsonResponse({
            "success": False,
            "message": "This email is already subscribed.",
        })
