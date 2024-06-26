from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):

    def test_home_view(self):
        """
        Test the home view.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')


class TestAboutView(TestCase):

    def test_about_view(self):
        """
        Test the about view.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')


class TestDeliveryView(TestCase):

    def test_delivery_view(self):
        """
        Test the delivery view.
        """
        response = self.client.get(reverse('delivery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/delivery.html')


class TestTermsView(TestCase):

    def test_terms_view(self):
        """
        Test the terms & conditions view view.
        """
        response = self.client.get(reverse('terms'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/terms.html')
