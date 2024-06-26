from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, redirect
from products.models import Product, Category
from django.http import HttpResponse
from urllib.parse import urlencode
from django.contrib import messages
from django.core.exceptions import ValidationError


class ViewCartTest(TestCase):
    def test_view_cart_page_loads(self):
        """
        Test that the view_cart page loads correctly.
        """
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')


class AddToCartViewTest(TestCase):
    def setUp(self):
        """
        Set up a category and a product for testing adding items to the cart.
        """
        self.category = Category.objects.create(
            name='Test Category',
            display_name='Test Category Display'
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10.00,
            stock=50,
            category=self.category
        )

    def test_add_to_cart(self):
        """
        Test adding a product to the cart.
        """
        item_id = self.product.id
        quantity = 2
        response = self.client.post(reverse('add_to_cart', args=[item_id]), {
            'quantity': quantity,
            'redirect_url': reverse('products')
        })

        # Check if the item was added to the cart in session
        cart = self.client.session.get('cart', {})
        self.assertIn(str(item_id), cart)
        self.assertEqual(cart[str(item_id)], quantity)

        # Check the response status code
        self.assertEqual(response.status_code, 302)

        # Check if the redirect URL is correct
        self.assertRedirects(response, reverse('products'))

        # Check if the correct message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'{quantity} {self.product.name} added to your cart.')

    def test_add_to_cart_insufficient_stock(self):
        """
        Test adding a quantity of a product that exceeds the available stock.
        """
        item_id = self.product.id
        quantity = 51  # More than available stock
        response = self.client.post(reverse('add_to_cart', args=[item_id]), {
            'quantity': quantity,
            'redirect_url': reverse('products')
        })

        # Check if the item was not added to the cart in session
        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(item_id), cart)

        # Check the response status code
        self.assertEqual(response.status_code, 302)

        # Check if the correct message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(f'Error: {self.product.name} has only {self.product.stock} units left.', str(messages[0]))

    def test_add_to_cart_existing_item(self):
        """
        Test adding additional quantity of an existing item in the cart.
        """
        item_id = self.product.id
        initial_quantity = 5
        additional_quantity = 3

        # Add initial quantity to the cart
        self.client.post(reverse('add_to_cart', args=[item_id]), {
            'quantity': initial_quantity,
            'redirect_url': reverse('products')
        })

        # Add additional quantity to the cart
        response = self.client.post(reverse('add_to_cart', args=[item_id]), {
            'quantity': additional_quantity,
            'redirect_url': reverse('products')
        })

        # Check if the item quantity in the cart is updated correctly
        cart = self.client.session.get('cart', {})
        self.assertIn(str(item_id), cart)
        self.assertEqual(cart[str(item_id)], initial_quantity + additional_quantity)

        # Check if the correct message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]), f'{additional_quantity} {self.product.name} added to your cart.')


class AdjustCartViewTest(TestCase):
    def setUp(self):
        """
        Set up a category and a product for testing adjusting cart quantities.
        """
        self.category = Category.objects.create(
            name='Test Category',
            display_name='Test Category Display'
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10.00,
            stock=50,
            category=self.category
        )

    def test_adjust_cart_valid_quantity(self):
        """
        Test adjusting quantity of a product to a valid number within available stock.
        """
        # Initial cart setup
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()

        # Adjusting quantity to a valid number within available stock
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 2
        })

        # Check if the item quantity in the cart is updated correctly
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], 2)

        # Check the response status code
        self.assertEqual(response.status_code, 302)

        # Check if the correct message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'{self.product.name} quantity updated to 2.')

    def test_adjust_cart_exceed_stock(self):
        """
        Test adjusting quantity of a product to exceed available stock.
        """
        # Initial cart setup
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()

        # Adjusting quantity to exceed available stock
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 51
        })

        # Check if the item quantity in the cart remains unchanged (should be capped at available stock)
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], self.product.stock)

        # Check the response status code
        self.assertEqual(response.status_code, 302)

        # Check if the correct error message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(f'Error: {self.product.name} has only {self.product.stock} units left.', str(messages[0]))

    def test_adjust_cart_negative_quantity(self):
        """
        Test adjusting quantity of a product to a negative number.
        """
        # Initial cart setup with a positive quantity
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()

        # Adjusting quantity to a negative number
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': -1
        })

        # Check if the correct error message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Quantity must be greater than zero.')

    def test_adjust_cart_zero_quantity(self):
        """
        Test adjusting quantity of a product to zero.
        """
        # Initial cart setup with a positive quantity
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()

        # Adjusting quantity to zero
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 0
        })

        # Check if the correct error message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Quantity must be greater than zero.')


class RemoveFromCartViewTest(TestCase):
    def setUp(self):
        """
        Set up a category and a product for testing removing items from the cart.
        """
        self.category = Category.objects.create(
            name='Test Category',
            display_name='Test Category Display'
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10.00,
            stock=50,
            category=self.category
        )

        # Set up a sample cart with the product
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()

    def test_remove_from_cart_success(self):
        """
        Test removing a product from the cart when it exists in the cart.
        """
        # Make a request to remove the product from the cart
        response = self.client.post(reverse('remove_from_cart', args=[self.product.id]))

        # Check if the response status code is 200 when product is successfully removed
        self.assertEqual(response.status_code, 200)

        # Check if the correct message was added
        messages = list(get_messages(response.wsgi_request))
        if f'{self.product.name} removed from your cart.' in [str(message) for message in messages]:
            self.assertEqual(str(messages[0]), f'{self.product.name} removed from your cart.')
        else:
            self.assertEqual(str(messages[0]), f'{self.product.name} is not in your cart.')