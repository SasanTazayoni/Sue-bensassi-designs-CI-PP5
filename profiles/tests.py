from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages


class TestUserProfileForm(TestCase):
    """ Test the UserProfileForm. """

    def test_empty_form_is_valid(self):
        """ All profile fields are optional so an empty form should be valid. """
        form = UserProfileForm({})
        self.assertTrue(form.is_valid())

    def test_valid_form_with_data(self):
        """ Test that a fully populated form is valid. """
        form = UserProfileForm({
            'default_phone_number': '1234567890',
            'default_street_address1': '123 Street',
            'default_street_address2': 'Apt 1',
            'default_town_or_city': 'Test City',
            'default_county': 'Test County',
            'default_postcode': 'TE1 1ST',
        })
        self.assertTrue(form.is_valid())

    def test_labels_are_removed(self):
        """ Test that all field labels are set to False. """
        form = UserProfileForm()
        for field in form.fields:
            self.assertFalse(form.fields[field].label)

    def test_autofocus_on_phone_number(self):
        """ Test that autofocus is set on the default_phone_number field. """
        form = UserProfileForm()
        self.assertTrue(
            form.fields['default_phone_number'].widget.attrs.get('autofocus')
        )

    def test_fields_have_correct_css_class(self):
        """ Test that all fields have the profile-form-input CSS class. """
        form = UserProfileForm()
        for field in form.fields:
            self.assertIn(
                'profile-form-input',
                form.fields[field].widget.attrs.get('class', '')
            )


class TestUserProfileModel(TestCase):
    """ Test the UserProfile model. """

    def test_str(self):
        """ Test string representation returns username. """
        user = User.objects.create_user('strtest', 'str@test.com', 'pass')
        self.assertEqual(str(user.userprofile), 'strtest')

    def test_profile_created_on_user_create(self):
        """ Test that a UserProfile is automatically created with a new user. """
        user = User.objects.create_user('newuser', 'new@test.com', 'pass')
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_profile_saved_on_user_update(self):
        """ Test that saving a user triggers profile save. """
        user = User.objects.create_user('updateuser', 'update@test.com', 'pass')
        user.first_name = 'Updated'
        user.save()
        # Profile should still exist and be accessible
        self.assertEqual(user.userprofile.user.first_name, 'Updated')


class TestProfileView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.user_profile, created = UserProfile.objects.get_or_create(user=self.user, defaults={'phone_number': '1234567890'})
        self.url = reverse('profile')

    def test_profile_view_authenticated_user(self):
        """
        Test profile view for authenticated user.
        """
        self.client.force_login(self.user)

        # GET request
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], UserProfileForm)
        self.assertIn('orders', response.context)
        orders = response.context['orders']
        self.assertTrue(all(order.user_profile == self.user_profile for order in orders))

    def test_profile_view_non_authenticated_user(self):
        """
        Test profile view for non-authenticated user.
        """
        # GET request
        response = self.client.get(self.url)
        
        # Check if the response is a redirect to login page
        self.assertRedirects(response, reverse('account_login') + '?next=' + self.url)
        
        # Since this is a redirect response, there won't be a context
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(response.context)

    def test_profile_view_post_valid(self):
        """ Test POST to profile view with valid data updates profile. """
        self.client.force_login(self.user)
        response = self.client.post(self.url, {
            'default_phone_number': '9999999999',
            'default_street_address1': '1 New Street',
            'default_street_address2': '',
            'default_town_or_city': 'New City',
            'default_county': '',
            'default_postcode': 'NE1 1ST',
        })
        self.assertEqual(response.status_code, 200)
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.default_phone_number, '9999999999')

    def test_profile_view_post_invalid(self):
        """ Test POST to profile view with invalid data shows error. """
        self.client.force_login(self.user)
        # phone_number has max_length=20, send 21 chars
        response = self.client.post(self.url, {
            'default_phone_number': 'x' * 21,
        })
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('error' in str(m).lower() or 'There was an error' in str(m) for m in messages))

    def test_order_history_view(self):
        """
        Test order history view.
        """
        # Create an Order instance
        order = Order.objects.create(order_number='12345')  # Replace with your Order creation logic

        # URL for order history view
        url = reverse('order_history', args=[order.order_number])

        # GET request
        response = self.client.get(url)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

        # Check context data
        self.assertIn('order', response.context)
        self.assertEqual(response.context['order'], order)
        self.assertIn('from_profile', response.context)
        self.assertTrue(response.context['from_profile'])
