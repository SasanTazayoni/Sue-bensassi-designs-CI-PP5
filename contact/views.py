from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


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
