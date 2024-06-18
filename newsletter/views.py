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
from .models import NewsletterSubscription
from .forms import NewsletterForm


def newsletter_subscribe(request):
    """ 
    A view to handle new sign ups to the newsletter mailing list.
    """

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            new_subscription = form.save()
            messages.success(
                request, 'You have subscribed to our mailing list.'
            )

            user_email = new_subscription.email
            subject = render_to_string(
                'newsletter/new_subscription_subject.txt')
            body = render_to_string(
                'newsletter/new_subscription_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL}
            )

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            return redirect(reverse('home'))

        else:
            errors = form.errors.get('email')
            if errors:
                if 'Newsletter subscription with this Email already exists.' in errors:
                    messages.warning(
                        request, 'This email has already subscribed to our mailing list.'
                    )
                else:
                    messages.error(
                        request, 'Failed to sign up. Please ensure the form is valid.'
                    )

    else:
        form = NewsletterForm()

    context = {
        'form': form,
    }

    return redirect(reverse('home'))
