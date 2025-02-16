from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BarberInfo, ServicesDes

# Register your models here.


@admin.register(BarberInfo)
class BarberInfoAdmin(SummernoteModelAdmin):
    """
    Admin interface for BarberInfo model.

    This class customizes the admin panel
    for the BarberInfo model by specifying
    the fields to be displayed in the list
    view, adding search functionality,
    and enabling Summernote for the 'description' field.
    """
    list_display = ('title', 'created_on', 'updated_on')
    search_fields = ('title',)
    summernote_fields = ('description',)

# Barber service modelu registeration


@admin.register(ServicesDes)
class ServicesDesAdmin(SummernoteModelAdmin):
    """
    Admin interface for ServicesDes model.

    This class customizes the admin panel for
    the ServicesDes model by specifying

    the fields to be displayed in the list view, adding search functionality,
    and enabling Summernote for the 'description' field.
    """
    list_display = ('title', 'created_on', 'updated_on')
    search_fields = ('title',)
    summernote_fields = ('description',)
