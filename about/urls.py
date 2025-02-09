from django.urls import path
from . import views

urlpatterns = [
    path('<int:barber_id>/', views.about_me, name='about_barber'),
    path('', views.about_me, name='about'),
]

