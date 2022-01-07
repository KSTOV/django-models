from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SnackTest(TestCase):
    def test_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

