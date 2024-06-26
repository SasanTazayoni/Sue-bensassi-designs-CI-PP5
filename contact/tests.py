from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from contact.forms import ContactForm
from contact.models import Enquiry


class TestContactView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_valid_form_submission(self):
        # Simulate a valid POST request with form data
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'enquiry': 'Test enquiry message.'
        }
        response = self.client.post(reverse('contact'), form_data)

        # Check redirection to contact_success page
        self.assertRedirects(response, reverse('contact_success'))

        # Check success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your enquiry has been sent successfully.')

        # Check that the enquiry is saved in the database
        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.first()
        self.assertEqual(enquiry.name, 'Test User')
        self.assertEqual(enquiry.email, 'test@example.com')
        self.assertEqual(enquiry.message, 'Test enquiry message.')

        # Check email sending
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New Enquiry from Test User')
        self.assertIn('Test enquiry message.', mail.outbox[0].body)

    def test_blank_form_submission(self):
        # Simulate a POST request with blank form data
        form_data = {}
        response = self.client.post(reverse('contact'), form_data)

        # Check that the form is not valid and user remains on contact.html
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The form data you entered was invalid.')

        # Check that no enquiry is saved
        self.assertEqual(Enquiry.objects.count(), 0)

        # Check that no email is sent
        self.assertEqual(len(mail.outbox), 0)

    def test_invalid_form_submission(self):
        # Simulate a POST request with invalid form data (missing 'email' field)
        form_data = {
            'name': 'Test User',
            'enquiry': 'Test enquiry message.'
        }
        response = self.client.post(reverse('contact'), form_data)

        # Check that the form is not valid and user remains on contact.html
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The form data you entered was invalid.')

        # Check that no enquiry is saved
        self.assertEqual(Enquiry.objects.count(), 0)

        # Check that no email is sent
        self.assertEqual(len(mail.outbox), 0)


class TestContactSuccessView(TestCase):

    def test_contact_success_view(self):
        # Issue a GET request to the contact_success view
        response = self.client.get(reverse('contact_success'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'contact/contact_success.html')
