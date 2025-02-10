from django.shortcuts import render
from .models import About
# from book.models import Barber
# from .forms import AboutForm

# Create your views here.
def about_me(request):
    abouts = About.objects.all()
    print(f"Total about entries: {abouts}")


    return render(
        request,
        "about/about.html",
        {
            "abouts": abouts,
        }
        )