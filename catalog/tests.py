from django.test import TestCase, Client
from django.urls import reverse


class CatalogViewsTestCase(TestCase):
    """Testing controllers (views) of the catalog application."""

    def setUp(self):
        """Initial settings for tests."""
        self.client = Client()

    def test_home_view(self):
        """We test that the main page opens and uses the correct template."""
        # 'catalog:home' is 'app_name:path_name' from urls.py
        url = reverse('catalog:home')
        response = self.client.get(url)

        # Check that the page returns code 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'catalog/home.html')

    def test_contacts_view_get(self):
        """We test that the contact page opens (GET) and uses the correct template."""
        url = reverse('catalog:contacts')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/contacts.html')

    def test_contacts_view_post(self):
        """We are testing that submitting a form (POST) to the contact page works."""
        url = reverse('catalog:contacts')
        # Data that we seem to send from the form
        form_data = {
            'name': 'Тестовый Юзер',
            'phone': '+79991234567',
            'message': 'Это тестовое сообщение.'
        }
        response = self.client.post(url, data=form_data)

        # After successfully submitting the form, the page should simply reload with the code 200
        self.assertEqual(response.status_code, 200)

        # We can't verify the print in the console,
        # but we have verified that our view processed the POST request without errors.
