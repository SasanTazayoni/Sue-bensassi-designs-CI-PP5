from unittest.mock import patch
from django.test import TestCase, override_settings
from django.urls import reverse
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product


class TestOrderForm(TestCase):
    """
    Test the validation of the OrderForm fields.
    """

    def test_valid_form(self):
        """ Test that a fully populated form is valid. """
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Test Street',
            'street_address2': '',
            'town_or_city': 'Test City',
            'postcode': 'TE1 1ST',
            'county': '',
        })
        self.assertTrue(form.is_valid())

    def test_optional_fields_not_required(self):
        """ Test that street_address2 and county are optional. """
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Test Street',
            'town_or_city': 'Test City',
            'postcode': 'TE1 1ST',
        })
        self.assertTrue(form.is_valid())

    def test_labels_are_removed(self):
        """ Test that all field labels are set to False. """
        form = OrderForm()
        for field in form.fields:
            self.assertFalse(form.fields[field].label)

    def test_autofocus_on_full_name(self):
        """ Test that autofocus is set on the full_name field. """
        form = OrderForm()
        self.assertTrue(form.fields['full_name'].widget.attrs.get('autofocus'))

    def test_required_fields_have_asterisk_in_placeholder(self):
        """ Test that required fields show * in their placeholder. """
        form = OrderForm()
        for field_name, field in form.fields.items():
            placeholder = form.fields[field_name].widget.attrs.get('placeholder', '')
            if field.required:
                self.assertIn('*', placeholder)
            else:
                self.assertNotIn('*', placeholder)

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


@override_settings(STRIPE_SECRET_KEY='sk_test_fake')
class TestCacheCheckoutData(TestCase):
    """ Test the cache_checkout_data view. """

    def test_get_request_not_allowed(self):
        """ Test that GET requests are rejected (view requires POST). """
        response = self.client.get(reverse('cache_checkout_data'))
        self.assertEqual(response.status_code, 405)

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_valid_post_returns_200(self, mock_modify):
        """ Test that a valid POST with client_secret returns 200. """
        session = self.client.session
        session['cart'] = {'1': 2}
        session.save()

        response = self.client.post(reverse('cache_checkout_data'), {
            'client_secret': 'pi_test_secret_key',
            'save_info': 'true',
        })

        self.assertEqual(response.status_code, 200)
        mock_modify.assert_called_once()

    @patch('checkout.views.stripe.PaymentIntent.modify', side_effect=Exception('Stripe error'))
    def test_stripe_error_returns_400(self, mock_modify):
        """ Test that a Stripe exception returns 400. """
        response = self.client.post(reverse('cache_checkout_data'), {
            'client_secret': 'pi_test_secret_key',
            'save_info': 'true',
        })
        self.assertEqual(response.status_code, 400)


class TestCheckoutView(TestCase):
    """ Test the checkout view. """

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test',
            price=10.00,
            stock=5,
        )
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

    def test_invalid_form_post_redirects_not_500(self):
        """ Test that a POST with an invalid form redirects to checkout rather than crashing. """
        response = self.client.post(reverse('checkout'), {
            'full_name': '',
            'client_secret': 'pi_test_secret_key',
        })
        self.assertRedirects(response, reverse('checkout'))


class TestOrderModel(TestCase):
    """ Test the Order model. """

    def test_order_number_generated_on_save(self):
        """ Test that order number is auto-generated on first save. """
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            street_address1='123 Street',
            town_or_city='Test City',
            postcode='TE1 1ST',
        )
        self.assertTrue(order.order_number)
        self.assertEqual(len(order.order_number), 32)

    def test_order_number_not_overwritten(self):
        """ Test that saving again does not change the order number. """
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            street_address1='123 Street',
            town_or_city='Test City',
            postcode='TE1 1ST',
        )
        original_number = order.order_number
        order.full_name = 'Updated Name'
        order.save()
        self.assertEqual(order.order_number, original_number)

    def test_order_str(self):
        """ Test the string representation of an order. """
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            street_address1='123 Street',
            town_or_city='Test City',
            postcode='TE1 1ST',
        )
        self.assertEqual(str(order), order.order_number)

    def test_update_total(self):
        """ Test that update_total correctly calculates grand total. """
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            street_address1='123 Street',
            town_or_city='Test City',
            postcode='TE1 1ST',
        )
        product = Product.objects.create(
            name='Test Product',
            description='Test',
            price=10.00,
            stock=10,
        )
        OrderLineItem.objects.create(order=order, product=product, quantity=3)
        order.refresh_from_db()
        self.assertEqual(order.grand_total, 30.00)


class TestOrderLineItemModel(TestCase):
    """ Test the OrderLineItem model. """

    def setUp(self):
        self.order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            street_address1='123 Street',
            town_or_city='Test City',
            postcode='TE1 1ST',
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Test',
            price=15.00,
            stock=10,
        )

    def test_lineitem_total_calculated_on_save(self):
        """ Test that lineitem_total is set correctly on save. """
        item = OrderLineItem.objects.create(
            order=self.order, product=self.product, quantity=2
        )
        self.assertEqual(item.lineitem_total, 30.00)

    def test_lineitem_str(self):
        """ Test the string representation of a line item. """
        item = OrderLineItem.objects.create(
            order=self.order, product=self.product, quantity=1
        )
        self.assertIn(self.product.name, str(item))
        self.assertIn(self.order.order_number, str(item))

    def test_signal_updates_order_total_on_delete(self):
        """ Test that deleting a line item updates the order total. """
        item = OrderLineItem.objects.create(
            order=self.order, product=self.product, quantity=2
        )
        self.order.refresh_from_db()
        self.assertEqual(self.order.grand_total, 30.00)
        item.delete()
        self.order.refresh_from_db()
        self.assertEqual(self.order.grand_total, 0)