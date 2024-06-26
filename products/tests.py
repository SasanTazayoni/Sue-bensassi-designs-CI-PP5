from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.paginator import Page
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os
from products.models import Product, Category
from products.forms import ProductForm


class TestProductsViewWithPagination(TestCase):
    """
    Test case for the all products view with pagination.
    """
    def setUp(self):
        """
        Set up test data.
        """
        # Create categories
        category_names = [
            'Photo Albums', 'Filing Chests', 'Key Holders', 
            'Memo Blocks', 'Photo Frames', 'Other Designs', 
            "Children's", 'Linen', 'Spots and Checks', 'Florals'
        ]
        self.categories = []
        for name in category_names:
            category = Category.objects.create(name=name)
            self.categories.append(category)

        # Create 30 products for testing pagination
        for i in range(30):
            category = self.categories[i % len(self.categories)]
            product = Product.objects.create(
                category=category,
                name=f'Test Product {i}',
                description=f'Test Description {i}',
                price=10.00 + i,
                stock=10,
            )

        # URL setup
        self.client = Client()
        self.products_list_url = reverse('products')  # Use 'products' instead of 'all_products'

    def test_all_products_pagination(self):
        """
        Test that products list view returns paginated products.
        """
        # Issue a GET request to products list view
        response = self.client.get(self.products_list_url)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that 'products' key exists in the context
        self.assertIn('products', response.context)

        # Retrieve paginated products from the context
        products = response.context['products']

        # Verify that products is an instance of Page (paginated queryset)
        self.assertIsInstance(products, Page)

        # Verify the expected number of products per page (default paginator is 12 per page)
        self.assertEqual(len(products), 12)

        # Verify that we have 30 products in total (from setUp method)
        self.assertEqual(Product.objects.count(), 30)

        # Verify the content of the first page of products
        self.assertEqual(products[0].name, 'Test Product 0')
        self.assertEqual(products[11].name, 'Test Product 11')

        # Example testing the second page if exists
        if products.has_next():
            response = self.client.get(self.products_list_url + '?page=2')
            self.assertEqual(response.status_code, 200)
            products = response.context['products']
            self.assertEqual(len(products), 12)  # Assuming 12 per page, adjust as necessary

        # Assert template used
        self.assertTemplateUsed(response, 'products/products.html')


class TestProductDetailView(TestCase):
    """
    Test case for the product_detail view.
    """
    def setUp(self):
        """
        Set up test data.
        """
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=19.99,
            stock=10,
        )
        self.product_id = self.product.pk
        self.client = Client()

    def test_product_detail_view(self):
        """
        Test product_detail view with a valid product_id.
        """
        # Issue a GET request to product_detail view
        response = self.client.get(reverse('product_detail', args=[self.product_id]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct product is rendered in the context
        self.assertIn('product', response.context)
        rendered_product = response.context['product']
        self.assertEqual(rendered_product, self.product)

        # Assert the correct template is used
        self.assertTemplateUsed(response, 'products/product_detail.html')


class TestAddProductView(TestCase):
    """
    Test case for the add_product view.
    """

    def setUp(self):
        """
        Set up test data.
        """
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        self.client = Client()
        self.client.force_login(self.user)

    def test_add_product_view_post_success(self):
        """
        Test POST request to add_product view with valid data.
        """
        # Prepare POST data
        post_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 19.99,
            'stock': 10,
            # Remove 'image' field from POST data
        }

        # Issue a POST request to add_product view
        response = self.client.post(reverse('add_product'), post_data)

        # Check that the response is a redirect (successful form submission)
        self.assertRedirects(response, reverse('product_detail', args=[1]))  # Adjust the args as per your product id

        # Check success message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully added the product!')

        # Check that the product was added to the database
        self.assertEqual(Product.objects.count(), 1)

    def test_add_product_view_post_fail_invalid_form(self):
        """
        Test POST request to add_product view with invalid data.
        """
        # Prepare POST data with invalid data
        post_data = {
            'name': '',
            'description': 'Test Description',
            'price': 19.99,
            'stock': 10,
            # Add any other required fields for your ProductForm
        }

        # Issue a POST request to add_product view with invalid data
        response = self.client.post(reverse('add_product'), post_data)

        # Check that the response is successful (validation error, same page reload)
        self.assertEqual(response.status_code, 200)

        # Check that the form is present in the context
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertIsInstance(form, ProductForm)

        # Check error message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to add product. Please ensure the form is valid.')

        # Check that no product was added to the database
        self.assertEqual(Product.objects.count(), 0)  # No product should be added

    def test_add_product_view_post_fail_not_superuser(self):
        """
        Test POST request to add_product view when user is not a superuser.
        """
        # Create a regular user
        regular_user = User.objects.create_user(
            username='test_user',
            email='user@test.com',
            password='test_password'
        )
        self.client.force_login(regular_user)

        # Prepare POST data
        post_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 19.99,
            'stock': 10,
            # Add any other required fields for your ProductForm
        }

        # Issue a POST request to add_product view as regular user
        response = self.client.post(reverse('add_product'), post_data)

        # Check that the response is a redirect (not authorized)
        self.assertRedirects(response, reverse('home'))

        # Check error message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You do not have permission to do that.')

        # Check that no product was added to the database
        self.assertEqual(Product.objects.count(), 0)


class TestEditProductView(TestCase):
    """
    Test case for the edit_product view.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.client = Client()

        # Create a superuser
        self.superuser = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        self.client.force_login(self.superuser)

        # Create a regular user
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='userpass'
        )

        # Create a product for testing
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=19.99,
            stock=10,
        )
        self.product_id = self.product.pk

    def test_edit_product_view_get_superuser(self):
        """
        Test GET request to edit product view for a superuser.
        """
        url = reverse('edit_product', args=[self.product_id])
        response = self.client.get(url)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'products/edit_product.html')

        # Check that the product is in the context
        self.assertIn('product', response.context)
        self.assertEqual(response.context['product'], self.product)

    def test_edit_product_view_get_normal_user(self):
        """
        Test GET request to edit product view for a normal user (should be denied).
        """
        # Create a regular user
        regular_user = User.objects.create_user(username='test_user', email='user@test.com', password='test_password')
        self.client.force_login(regular_user)

        url = reverse('edit_product', args=[self.product_id])
        response = self.client.get(url)

        # Check that the response is a redirect (normal user should be denied)
        self.assertRedirects(response, reverse('home'))

        # Check for an error message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You do not have permission to do that.')

        # Ensure that the product is not editable by a normal user
        product = Product.objects.get(pk=self.product_id)
        self.assertEqual(product.name, 'Test Product')

    def test_edit_product_view_post_success(self):
        """
        Test POST request to edit product view with valid data.
        """
        url = reverse('edit_product', args=[self.product_id])
        post_data = {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'price': 25.99,
            'stock': 15,
        }

        response = self.client.post(url, post_data)

        # Check that the response is a redirect (successful form submission)
        self.assertRedirects(response, reverse('product_detail', args=[self.product_id]))

        # Check success message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Updated the product details!')

        # Refresh the product from the database and check updated fields
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.description, 'Updated Description')
        self.assertEqual(float(self.product.price), 25.99)
        self.assertEqual(self.product.stock, 15)

    def test_edit_product_view_post_fail_invalid_form(self):
        """
        Test POST request to edit product view with invalid data.
        """
        url = reverse('edit_product', args=[self.product_id])
        post_data = {
            'name': '',  # Invalid: Name is required
            'description': 'Updated Description',
            'price': 25.99,
            'stock': 15,
        }

        response = self.client.post(url, post_data)

        # Check that the response is successful (validation error, same page reload)
        self.assertEqual(response.status_code, 200)

        # Check that the form is present in the context
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertIsInstance(form, ProductForm)

        # Check for at least one error message
        messages = list(get_messages(response.wsgi_request))
        self.assertGreater(len(messages), 0)

        # Refresh the product from the database and ensure no changes were made
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(float(self.product.price), 19.99)
        self.assertEqual(self.product.stock, 10)

    def test_edit_product_view_get_unauthenticated(self):
        """
        Test GET request to edit product view when user is not authenticated.
        """
        self.client.logout()
        url = reverse('edit_product', args=[self.product_id])
        response = self.client.get(url)

        # Check that the response is a redirect (to login page)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

        # Ensure the product details remain unchanged
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(float(self.product.price), 19.99)
        self.assertEqual(self.product.stock, 10)


class TestDeleteProductView(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.client.force_login(self.superuser)
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=19.99,
            stock=10,
        )

    def test_delete_product_superuser(self):
        """
        Test DELETE request to delete product view as a superuser.
        """
        url = reverse('delete_product', args=[self.product.id])
        response = self.client.delete(url)

        # Check that the product is deleted
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete
        self.assertEqual(Product.objects.filter(pk=self.product.id).exists(), False)

        # Check success message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product removed!')

    def test_delete_product_normal_user(self):
        """
        Test DELETE request to delete product view as a normal user (should be denied).
        """
        normal_user = User.objects.create_user('user', 'user@example.com', 'userpassword')
        self.client.force_login(normal_user)

        url = reverse('delete_product', args=[self.product.id])
        response = self.client.delete(url)

        # Check that the response is a redirect (normal user should be denied)
        self.assertEqual(response.status_code, 302)  # Redirected to home page

        # Check for an error message in messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You do not have permission to do that.')

        # Ensure that the product is not deleted
        self.assertTrue(Product.objects.filter(pk=self.product.id).exists())
