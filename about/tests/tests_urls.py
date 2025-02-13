from django.test import SimpleTestCase
from django.urls import resolve, reverse
from about.views import about_me

# Create your tests here.
class AboutURLsTest(SimpleTestCase):

    def test_about_url_resolves(self):
        """Test if the about URL correctly resolves to the about_me view."""
        url = reverse('about')  # Should match the name in urlpatterns
        self.assertEqual(resolve(url).func, about_me)
