from django.test import TestCase

from django.test import SimpleTestCase
from django.urls import reverse


class ThingsTests(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_about_page_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')