from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import About, Collaboration
from .forms import CollaborationForm

def about_me(request):
    abouts = About.objects.all()
    print(f"Total about entries: {abouts}")

    collaborations = Collaboration.objects.all()
    forms = CollaborationForm()
    maps_api = settings.API_KEY
    

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
            print("-" * 20)
    else:
        print("Not found collaborations")

    if request.method == "POST":
        forms = CollaborationForm(data=request.POST)
        if forms.is_valid():
            collaborations = forms.save(commit=False)
            collaborations.request = request.user
            collaborations.save()
            messages.add_message(
                request, messages.SUCCESS,
                "You're collaboration request is succesfully send, will be in touch in two days")
            return redirect('about')

        else:
            messages.add_message(
                request, messages.ERROR,
                "There was an error with your form submission. Please check the details and try again.")



    return render(
        request,
        "about/about.html",
        {
            "abouts": abouts,
            "forms": forms,
            "collaborations": collaborations,
            "maps_api": maps_api,
        }
        )