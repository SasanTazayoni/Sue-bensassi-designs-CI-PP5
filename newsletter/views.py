from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import NewsletterSubscription
from .forms import NewsletterForm


def newsletter_subscribe(request):
    """ 
    A view to handle new sign ups to the newsletter mailing list.
    """

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have subscribed to our mailing list.'
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
