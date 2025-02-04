from django.urls import path
from . import views

#Booking app path
urlpatterns = [
    # path('', views.BookCoverShow.as_view(), name='book'),
    path('form/', views.booking_form_view, name='book'),
]