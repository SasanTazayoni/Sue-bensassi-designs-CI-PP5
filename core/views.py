from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):
    """ Renders the home page. """

    return render(request, 'core/index.html')


def about(request):
    """ Renders the about page. """

    return render(request, 'core/about.html')


def delivery(request):
    """ Renders the delivery page. """

    return render(request, 'core/delivery.html')


def terms(request):
    """ Renders the terms & conditions page. """

    return render(request, 'core/terms.html')


def contact(request):
    """ Renders the contact page and handles form submission. """
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            enquiry = form.cleaned_data['enquiry']
            
            subject = f"New Enquiry from {name}"
            message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{enquiry}"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )
            
            return redirect('contact_success')
    
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def contact_success(request):
    """ Renders the contact success page. """

    return render(request, 'core/contact_success.html')
