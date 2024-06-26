from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from contact.forms import ContactForm
from contact.models import Enquiry


class TestContactView(TestCase):
    """
    Test case for the contact view.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_valid_form_submission(self):
        """
        Test valid form submission in the contact view.
        """
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'enquiry': 'Test enquiry message.'
        }
        response = self.client.post(reverse('contact'), form_data)

        self.assertRedirects(response, reverse('contact_success'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your enquiry has been sent successfully.')

        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.first()
        self.assertEqual(enquiry.name, 'Test User')
        self.assertEqual(enquiry.email, 'test@example.com')
        self.assertEqual(enquiry.message, 'Test enquiry message.')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New Enquiry from Test User')
        self.assertIn('Test enquiry message.', mail.outbox[0].body)

    def test_blank_form_submission(self):
        """
        Test blank form submission in the contact view.
        """
        form_data = {}
        response = self.client.post(reverse('contact'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The form data you entered was invalid.')

        self.assertEqual(Enquiry.objects.count(), 0)

        self.assertEqual(len(mail.outbox), 0)

    def test_invalid_form_submission(self):
        """
        Test invalid form submission in the contact view.
        """
        form_data = {
            'name': 'Test User',
            'enquiry': 'Test enquiry message.'
        }
        response = self.client.post(reverse('contact'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The form data you entered was invalid.')

        self.assertEqual(Enquiry.objects.count(), 0)

        self.assertEqual(len(mail.outbox), 0)


class TestContactSuccessView(TestCase):
    """
    Test case for the contact success view.
    """
    def test_contact_success_view(self):
        """
        Test the contact success view.
        """
        response = self.client.get(reverse('contact_success'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'contact/contact_success.html')
