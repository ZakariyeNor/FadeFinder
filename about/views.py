from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import About, Collaboration
from .forms import CollaborationForm

def about_me(request):
    
    abouts = About.objects.all()

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