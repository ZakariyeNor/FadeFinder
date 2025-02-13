from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from ..models import About, Collaboration

# Create your tests here.
class AboutMeViewTest(TestCase):
    
    def test_about_me_view_status_code(self):
        """Test if the about_me view returns a 200 status code."""
        response = self.client.get(reverse('about'))  # Ensure this matches the URL pattern name
        self.assertEqual(response.status_code, 200)

    def test_about_me_view_template_used(self):
        """Test if the about_me view uses the correct template."""
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')  # Replace with actual template name


