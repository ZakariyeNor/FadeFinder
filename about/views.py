from django.shortcuts import render,get_object_or_404
from .models import About
from book.models import Barber
from .forms import AboutForm

# Create your views here.
def about_me(request):
    abouts = About.objects.all()
    form = AboutForm()

    about_info = None
    barber = None

    if request.method == "POST":
        barber_id = request.POST.get('barber_id')
    else:
        barber_id = None

    if barber_id:
        barber = get_object_or_404(Barber, id=barber_id)
        about_info = About.objects.filter(about_barber=barber).first()


    return render(
        request,
        "about/about.html",
        {
            "form": form,
            "abouts": abouts,
            "barber": barber,
            "about_info": about_info,
            "no_barber_selected": not barber,
        }
        )