from django.shortcuts import render
from .models import About, Collaboration
from .forms import CollaborationForm
# from book.models import Barber
# from .forms import AboutForm

# Create your views here.
def about_me(request):
    abouts = About.objects.all()
    print(f"Total about entries: {abouts}")

    collaborations = Collaboration.objects.all()
    forms = CollaborationForm()

    if collaborations:
        total_collaborations = collaborations.count()
        print(f"Total Collaborations: {total_collaborations}")
        

        for collaboration in collaborations:
            print(f"Barber Name: {collaboration.barber_name}")
            print(f"Barber Shop: {collaboration.barber_shop}")
            print(f"Business Type: {collaboration.business_type}")
            print(f"Service Offered: {collaboration.service_offered}")
            print(f"Email: {collaboration.email}")
            print(f"Phone Number: {collaboration.number}")
            print(f"Additional Info: {collaboration.more_info}")
            print(f"Created On: {collaboration.created_on}")
            print(f"Updated On: {collaboration.updated_on}")
            print("-" * 20)
    else:
        print("Not found collaborations")


    return render(
        request,
        "about/about.html",
        {
            "abouts": abouts,
            "collaborations": collaborations,
        }
        )