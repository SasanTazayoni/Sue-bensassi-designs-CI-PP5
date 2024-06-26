from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from newsletter.models import NewsletterSubscription


class TestNewsletterSubscribeView(TestCase):
    """
    Test case for the newsletter subscribe view.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_valid_form_submission(self):
        """
        Test valid form submission in the newsletter_subscribe view.
        """
        form_data = {
            'email': 'test@example.com',
        }
        response = self.client.post(reverse('newsletter_subscribe'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"success": True, "message": "Thank you for subscribing!"}
        )

        self.assertEqual(NewsletterSubscription.objects.count(), 1)
        subscription = NewsletterSubscription.objects.first()
        self.assertEqual(subscription.email, 'test@example.com')

    def test_invalid_form_submission(self):
        """
        Test invalid form submission in the newsletter_subscribe view.
        """
        form_data = {}
        response = self.client.post(reverse('newsletter_subscribe'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"success": False, "message": "A valid Email is required."}
        )

        self.assertEqual(NewsletterSubscription.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)

    def test_blank_form_submission(self):
        """
        Test blank form submission in the newsletter_subscribe view.
        """
        form_data = {'email': ''}
        response = self.client.post(reverse('newsletter_subscribe'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"success": False, "message": "A valid Email is required."}
        )

        self.assertEqual(NewsletterSubscription.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)

    def test_duplicate_email_submission(self):
        """
        Test submitting a duplicate email in the newsletter_subscribe view.
        """
        # Create a subscription with the email first
        NewsletterSubscription.objects.create(email='test@example.com')

        # Attempt to subscribe again with the same email
        form_data = {'email': 'test@example.com'}
        response = self.client.post(reverse('newsletter_subscribe'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"success": False, "message": "This email is already subscribed."}
        )
