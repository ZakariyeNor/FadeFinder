from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class BarberInfoContentTest(TestCase):

    def test_view_url(self):
        # The correct URL name should be
        # 'home' as defined in your urls.py
        
        url = reverse('home')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
