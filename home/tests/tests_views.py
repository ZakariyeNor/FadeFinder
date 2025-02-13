from django.test import TestCase
from django.urls import reverse
from ..models import BarberInfo, ServicesDes


# Create your tests here.
#Home page generic view
class BarberInfoContentTest(TestCase):
    
    def setUp(self):
        # Create a sample BarberInfo object
        BarberInfo.objects.create(
            title="Barber Shop 1", 
            description="Best barber shop in town"
        )
        # Create a sample ServicesDes object
        ServicesDes.objects.create(
            title="Haircut", 
            services="Full haircut and shave"
        )

    
    def test_view_url(self):
        # Test that the view URL renders correctly
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_context(self):
        # Test that the context contains the correct data
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('barberinfo', response.context)
        self.assertIn('servicedescription', response.context)

    def test_view_template(self):
        # Test that the correct template is being used
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/home.html')