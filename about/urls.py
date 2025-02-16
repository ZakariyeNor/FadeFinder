from django.urls import path
from . import views

#Url path for about app
urlpatterns = [
    path('', views.about_me, name='about'),
]
