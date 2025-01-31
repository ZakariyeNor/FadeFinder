from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookCoverShow.as_view(), name='book'),
]