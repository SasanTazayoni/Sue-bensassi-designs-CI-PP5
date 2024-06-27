from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Enquiry
from profiles.models import UserProfile


def contact(request):
    """ Renders the contact page and handles form submission. """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                Enquiry.objects.create(
                    name=name,
                    email=email,
                    message=message,
                    user_profile=user_profile
                )
            else:
                Enquiry.objects.create(name=name, email=email, message=message)

            subject = f"New Enquiry from {name}"
            message_content = (
                f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )
            try:
                send_mail(
                    subject,
                    message_content,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                )
                messages.success(
                    request,
                    'Your enquiry has been sent successfully.'
                )
                return redirect('contact_success')
            except Exception as e:
                messages.error(
                    request,
                    f'There was an error sending your enquiry.'
                    f'Please try again later.'
                )
        else:
            messages.error(
                request,
                f'The form data you entered was invalid.'
                f'Please check the form and try again.'
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


def edit_enquiry(request, enquiry_id):
    """ Edit an existing enquiry. """

    enquiry = get_object_or_404(Enquiry, pk=enquiry_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Update enquiry fields with form data
            enquiry.name = form.cleaned_data['name']
            enquiry.email = form.cleaned_data['email']
            enquiry.message = form.cleaned_data['message']
            enquiry.save()
            return redirect('profile')
    else:
        form = ContactForm(initial={
            'name': enquiry.name,
            'email': enquiry.email,
            'message': enquiry.message,
        })

    return render(
        request,
        'contact/edit_enquiry.html', {'form': form, 'enquiry_id': enquiry_id}
    )


@login_required
def delete_enquiry(request, enquiry_id):
    """ Delete an existing enquiry. """

    enquiry = get_object_or_404(
        Enquiry, id=enquiry_id, user_profile__user=request.user
    )

    if request.method == 'POST':
        enquiry.delete()
        messages.success(request, 'Enquiry deleted successfully.')
        return redirect('profile')

    context = {
        'enquiry': enquiry,
    }
    return render(request, 'contact/delete_enquiry.html', context)
