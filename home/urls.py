from . import views
from django.urls import path

urlpatterns = [
    path('', views.BarberInfoContent.as_view(), name='home'),
]
