from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Collaboration
from book.models import Booking
from .forms import CollaborationForm

#about me views for about template
def about_me(request):

    """
    Handle the About page view.

    This view retrieves and displays information
    about the website or business.
    It also allows authenticated users to view their
    bookings and submit a 
    collaboration request.

    - Retrieves `About` details and collaboration records.
    - Shows user bookings if authenticated.
    - Displays a collaboration form and processes submissions.
    - Handles success/error messages and redirects on form submission.
    - Passes relevant data, including the Google Maps API key,
    to the template.

    """

    abouts = About.objects.all()
    bookings = Booking.objects.filter(
        user=request.user) if request.user.is_authenticated else []

    maps_api = settings.API_KEY

    collaborations = Collaboration.objects.all()

    forms = CollaborationForm()

    if request.method == "POST":
        forms = CollaborationForm(data=request.POST)
        if forms.is_valid():
            collaborations = forms.save(commit=False)
            collaborations.request = request.user
            collaborations.save()
            messages.add_message(
                request, messages.SUCCESS,
                "You're collaboration request is succesfully send,"
                "will be in touch in two days")
            return redirect('about')
        else:
            messages.add_message(
                request, messages.ERROR,
                "There was an error with your form"
                "submission. Please check the details and try again."
            )

    return render(
            request,
            "about/about.html",
            {
                "abouts": abouts,
                "forms": forms,
                "collaborations": collaborations,
                "maps_api": maps_api,
                "bookings": bookings,
            }
            )
