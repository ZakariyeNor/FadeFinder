from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import reverse
from django.templatetags.static import static


class BarberBookingTemplateTest(TestCase):

    # Test if the template renders correctly with barber and service context
    def test_barber_booking_template_renders(self):
        context = {
            'barberinfo': [
                {
                    'title': 'Barber 1',
                    'description': 'Description 1',
                    'image': 'image1.jpg',
                    'created_on': '2025-02-14'
                },
                {
                    'title': 'Barber 2',
                    'description': 'Description 2',
                    'image': 'image2.jpg',
                    'created_on': '2025-02-13'
                },
            ],
            'servicedescription': [
                {
                    'title': 'Haircut',
                    'services': 'Basic haircut service',
                    'image': 'service1.jpg',
                    'created_on': '2025-02-14'
                },
                {
                    'title': 'Shave',
                    'services': 'Shaving service',
                    'image': 'service2.jpg',
                    'created_on': '2025-02-12'
                },
            ],
        }

        # Render the template with the context
        html_output = render_to_string('home/home.html', context)

        # Write the HTML output to a file inside the home/tests/ directory
        with open('home/tests/output_home', 'w', encoding='utf-8') as f:
            f.write(html_output)

        # Check if the title block is rendered
        self.assertIn('<title>Barber Booking</title>', html_output)

        # Check if the barber information is correctly rendered
        self.assertIn('<h3>Barber 1</h3>', html_output)
        self.assertIn('<p>Description 1</p>', html_output)
        self.assertIn('<h3>Barber 2</h3>', html_output)
        self.assertIn('<p>Description 2</p>', html_output)

        # Check if the service description is correctly rendered
        self.assertIn('<h3>Haircut</h3>', html_output)
        self.assertIn('<p>Basic haircut service</p>', html_output)

    # Test if the updated date is displayed correctly for barber and service
    def test_updated_on_date_displayed(self):
        context = {
            'barberinfo': [
                {
                    'title': 'Barber 1',
                    'description': 'Description',
                    'image': 'image1.jpg',
                    'created_on': '2025-02-14'
                }],
            'servicedescription': [
                {
                    'title': 'Shampoo',
                    'services': 'Shampoo service',
                    'image': 'service1.jpg',
                    'created_on': '2025-02-15'
                }],
        }

        html_output = render_to_string('home/home.html', context)

        # Check if the updated date for barber is displayed
        self.assertIn('Updated on: 2025-02-14', html_output)

        # Check if the updated date for service is displayed
        self.assertIn('Updated on: 2025-02-15', html_output)

    # Test if the content block 'content' is correctly filled
    def test_content_block_rendered(self):
        context = {
            'barberinfo': [
                {
                    'title': 'Barber 1',
                    'description': 'Description',
                    'image': 'image1.jpg',
                    'created_on': '2025-02-14'
                }],
            'servicedescription': [
                {
                    'title': 'Shampoo',
                    'services': 'Shampoo service',
                    'image': 'service1.jpg',
                    'created_on': '2025-02-15'
                }],
        }

        html_output = render_to_string('home/home.html', context)

        # Check if the content block contains barber information
        self.assertIn('<h3>Barber 1</h3>', html_output)
        self.assertIn('<p>Description</p>', html_output)

        # Check if the content block contains service information
        self.assertIn('<h3>Shampoo</h3>', html_output)
        self.assertIn('<p>Shampoo service</p>', html_output)

    # Test if the page inherits base.html correctly (Check the nav and footer)
    def test_template_inheritance(self):
        response = self.client.get(reverse('home'))
        self.assertContains(
            response, '<nav class="navbar navbar-expand-lg primary-bg">')
        self.assertContains(
            response,
            '<footer class="container-fluid'
            'text-color-sec pt-4 fixed-bottom">'
        )

    # HTML validation (check if the rendered HTML is valid)
    def test_render_template_for_validation(self):
        context = {
            'barberinfo': [
                {
                    'title': 'Barber 1',
                    'description': 'Description',
                    'image': 'image1.jpg',
                    'created_on': '2025-02-14'
                }],
            'servicedescription': [
                {
                    'title': 'Shampoo',
                    'services': 'Shampoo service',
                    'image': 'service1.jpg',
                    'created_on': '2025-02-15'
                }],
        }

        html_output = render_to_string('home/home.html', context)
