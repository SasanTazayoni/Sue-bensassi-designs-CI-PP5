from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Enquiry


def contact(request):
    """ Renders the contact page and handles form submission. """
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            enquiry = form.cleaned_data['enquiry']

            Enquiry.objects.create(name=name, email=email, message=enquiry)
            
            subject = f"New Enquiry from {name}"
            message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{enquiry}"
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                )
                messages.success(request, 'Your enquiry has been sent successfully.')
                return redirect('contact_success')
            except Exception as e:
                messages.error(
                    request, 'There was an error sending your enquiry. \
                        Please try again later.'
                )
    
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """ Renders the contact success page. """

    return render(request, 'contact/contact_success.html')
