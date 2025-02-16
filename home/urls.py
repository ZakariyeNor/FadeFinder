from . import views
from django.urls import path

#Home page url
urlpatterns = [
    path('', views.BarberInfoContent.as_view(), name='home'),
]
