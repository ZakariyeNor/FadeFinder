from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import reverse
from django.templatetags.static import static
from django.contrib.messages import get_messages
from django.contrib import messages

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


    #Test correct links for unauthenticated users
    def test_links_for_unauthenticated_users(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Book')
        self.assertContains(response, 'Register')
        self.assertNotContains(response, 'Log-out')
        self.assertNotContains(response, 'Admin-Log-out')


    #Test if static filesexternal resources are included in the template
    def test_static_files_included(self):
        
        # Get the home page response
        response = self.client.get(reverse('home'))
        
        # Check if the external CSS file is included
        self.assertContains(response, 'href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"')
        self.assertContains(response, 'href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css"')

        # Check if the static CSS file is included
        self.assertContains(response, 'href="{}"'.format(static('css/style.css')))
        
        # Check if the external JS files are included
        self.assertContains(response, 'src="https://kit.fontawesome.com/44dbf25b5c.js"')
        self.assertContains(response, 'src="https://code.jquery.com/jquery-3.7.1.min.js"')
        self.assertContains(response, 'src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"')
        self.assertContains(response, 'src="https://cdn.jsdelivr.net/npm/flatpickr"')

        # Check if the static JS file is included
        self.assertContains(response, 'src="{}"'.format(static('js/script.js')))


    #Test if success/error messages are displayed correctly
    def test_messages_displayed(self):


        response = self.client.get(reverse('home'))
        self.client.get(reverse('home'))
        
        
        message = "Successfully logged in!"
        messages.success(response.wsgi_request, message)
        storage = get_messages(response.wsgi_request)
        
        # Check if the message exists in the response
        self.assertTrue(any(msg.message == message for msg in storage))

    #Test if child templates inherit base.html correctly
    def test_template_inheritance(self):
        
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<nav class="navbar navbar-expand-lg primary-bg">')
        self.assertContains(response, '<footer class="container-fluid text-color-sec pt-4 fixed-bottom">')



    #HTML validation
    def test_render_base_template(self):
        
        # Render the template
        html_output = render_to_string('base.html')
        
        context = {
            'servicedescription': 'Description of the service',
            'barberinfo': 'Information about the barber',
            }
            
        # Render the base template with the context
        html_output = render_to_string('base.html', context)

        # Write the HTML output to a file for inspection
        with open('tests/output_base.html', 'w', encoding='utf-8') as f:
            f.write(html_output)
                
       
       # Example assertions to check that important elements are present
        self.assertIn('<meta charset="UTF-8">', html_output)
        self.assertIn('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"', html_output)
        self.assertIn('<a class="navbar-brand text-color-sec" href="/">Barber Booking</a>', html_output)  # Change here
        self.assertIn('<footer class="container-fluid text-color-sec pt-4 fixed-bottom">', html_output)