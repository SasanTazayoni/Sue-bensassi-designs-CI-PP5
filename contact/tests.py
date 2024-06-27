from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from contact.forms import ContactForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
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
            'message': 'Test enquiry message.'  # Update the field name to 'message'
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


class EditEnquiryViewTests(TestCase):
    """ Test cases for the edit enquiry view. """

    def setUp(self):
        """ Set up test data before each test method execution. """
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a sample enquiry associated with the logged-in user
        self.enquiry = Enquiry.objects.create(
            name='Test Enquiry',
            email='test@example.com',
            message='This is a test enquiry.',
            date_sent=timezone.now(),
            replied_to=False,
            user_profile=None  # Assuming user_profile is optional in your model
        )

    def test_get_edit_enquiry(self):
        """ Test GET request to edit an existing enquiry. """
        # Issue a GET request to edit an existing enquiry
        response = self.client.get(reverse('edit_enquiry', args=[self.enquiry.id]))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the form is rendered with correct initial data
        form = response.context['form']
        self.assertIsInstance(form, ContactForm)
        self.assertEqual(form.initial['name'], self.enquiry.name)
        self.assertEqual(form.initial['email'], self.enquiry.email)
        self.assertEqual(form.initial['message'], self.enquiry.message)

    def test_post_edit_enquiry(self):
        """ Test POST request to update an existing enquiry. """
        # Prepare POST data with updated information
        updated_data = {
            'name': 'Updated Name',
            'email': 'updated@example.com',
            'message': 'This is an updated message.',
        }

        # Issue a POST request to update the enquiry
        response = self.client.post(reverse('edit_enquiry', args=[self.enquiry.id]), updated_data)

        # Check if the form submission redirects to the 'profile' page
        self.assertRedirects(response, reverse('profile'))

        # Refresh the enquiry object from the database
        self.enquiry.refresh_from_db()

        # Check if the enquiry object is updated correctly
        self.assertEqual(self.enquiry.name, updated_data['name'])
        self.assertEqual(self.enquiry.email, updated_data['email'])
        self.assertEqual(self.enquiry.message, updated_data['message'])

    def test_invalid_post_edit_enquiry(self):
        """ Test POST request with invalid data to edit an existing enquiry. """
        # Prepare POST data with invalid information (missing required field)
        invalid_data = {
            'name': 'Updated Name',
            'email': '',  # Invalid email
            'message': 'This is an updated message.',
        }

        # Issue a POST request with invalid data
        response = self.client.post(reverse('edit_enquiry', args=[self.enquiry.id]), invalid_data)

        # Check if the form renders back with errors
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'This field is required.')

        # Refresh the enquiry object from the database and ensure it's not changed
        self.enquiry.refresh_from_db()
        self.assertNotEqual(self.enquiry.name, invalid_data['name'])
        self.assertNotEqual(self.enquiry.message, invalid_data['message'])


class DeleteEnquiryViewTests(TestCase):
    """ Test cases for the delete_enquiry view. """

    def setUp(self):
        """ Set up test data before each test method execution. """
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a sample enquiry associated with the logged-in user
        self.enquiry = Enquiry.objects.create(
            name='Test Enquiry',
            email='test@example.com',
            message='This is a test enquiry.',
            date_sent=timezone.now(),
            replied_to=False,
            user_profile=self.user.userprofile
        )

    def test_delete_enquiry_success(self):
        """ Test POST request to delete an existing enquiry. """
        # Issue a POST request to delete the enquiry
        response = self.client.post(reverse('delete_enquiry', args=[self.enquiry.id]))

        # Check if the enquiry is deleted from the database
        self.assertFalse(Enquiry.objects.filter(id=self.enquiry.id).exists())

        # Check if the user is redirected to 'profile' after deletion
        self.assertRedirects(response, reverse('profile'))

        # Check if success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Enquiry deleted successfully.')
