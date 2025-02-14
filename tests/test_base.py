from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import reverse

class BaseTemplateTest(TestCase):

    #Test if the base.html template renders correctly.
    def test_base_template_renders(self):
        html_output = render_to_string('base.html', {'user': None})

        self.assertIn('<title>', html_output)
        self.assertIn('Barber Booking', html_output)
        self.assertIn('<nav', html_output)
        self.assertIn('<footer', html_output)
        self.assertIn('Login', html_output)
    
    #Test if it shows the logout option when user is authenticated
    def test_authenticated_user_in_template(self):
        self.client.force_login(self.create_test_user())
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Log-out')

    def create_test_user(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.create_user(username='username', password='uspassword')

    #Test nav links for the in logged users
    def test_links_for_authenticated_users(self):
        self.client.force_login(self.create_test_user())
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Log-out')
        self.assertContains(response, 'Admin')
        self.assertNotContains(response, 'Login')
        self.assertNotContains(response, 'Register')

    def test_links_for_unauthenticated_users(self):
        """Test correct links for unauthenticated users."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Book')
        self.assertContains(response, 'Register')
        self.assertNotContains(response, 'Log-out')
        self.assertNotContains(response, 'Admin-Log-out')