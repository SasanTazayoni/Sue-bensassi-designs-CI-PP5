from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages


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
