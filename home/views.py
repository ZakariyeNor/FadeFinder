from django.shortcuts import render
from django.views import generic
from .models import BarberInfo, ServicesDes


# Create your views here.
class BarberInfoContent(generic.ListView):
    model = BarberInfo
    template_name = 'home/home.html'
    context_object_name = 'barberinfo'


    # def ServicesDescription(request):
    #     servicedescription = ServicesDes.objects.all()
    #     return render(
    #         request,
    #         'home/home.html',
    #         {'servicedescription': servicedescription},
    # )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicedescription'] = ServicesDes.objects.all()
        return context
