from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test the validation of the OrderForm fields.
    """

    def test_full_name_required(self):
        """
        Test that the 'full_name' field in OrderForm is required.
        """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.'
        )

    def test_email_required(self):
        """
        Test that the 'email' field in OrderForm is required.
        """
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.'
        )

    def test_phone_number_required(self):
        """
        Test that the 'phone_number' field in OrderForm is required.
        """
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.'
        )

    def test_postcode_required(self):
        """
        Test that the 'postcode' field in OrderForm is required.
        """
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(
            form.errors['postcode'][0], 'This field is required.'
        )
    
    def test_town_or_city_required(self):
        """
        Test that the 'town_or_city' field in OrderForm is required.
        """
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.'
        )

    def test_street_address1_required(self):
        """
        Test that the 'street_address1' field in OrderForm is required.
        """
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.'
        )