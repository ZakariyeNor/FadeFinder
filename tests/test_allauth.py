from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AllAuthTests(TestCase):
    def setUp(self):
        """Setup a test user."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

    def test_signup(self):
        """Test the signup process."""
        url = reverse('account_signup')
        response = self.client.post(url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login(self):
        """Test login process."""
        url = reverse('account_login')
        response = self.client.post(url, {
            'login': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_logout(self):
        """Test logout process."""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('accounts_logout/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_signup_invalid(self):
        """Test signup with invalid data."""
        url = reverse('account_signup')
        response = self.client.post(url, {
            'username': 'invaliduser',
            'email': 'invalidemail',
            'password1': 'short',
            'password2': 'short',
        })

        self.assertEqual(response.status_code, 200)

        # Assert email error
        form = response.context['form']
        self.assertTrue(form.errors['email'])
        self.assertIn('Enter a valid email address.', form.errors['email'])

        # Assert password error (update to match the full error message)
        self.assertTrue(form.errors['password1'])
        self.assertIn(
            'This password is too short. It must contain'
            ' at least 8 characters.', form.errors['password1']
        )
