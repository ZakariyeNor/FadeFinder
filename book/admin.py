from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BookCover, Barber, BarberService, Booking


@admin.register(BookCover)
class BookCoverAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the BookCover model.
    Allows editing of the 'booking_intro' field using Summernote editor.
    """
    summernote_fields = ('booking_intro',)


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Barber model.
    Allows search by 'barber_name' and displays 'barber_name',
    'barber_address', and 'barber_number' in the list view.
    Filters the list by 'updated_on' and 'created_on'.
    """
    search_fields = ['barber_name']
    list_display = ('barber_name', 'barber_address', 'barber_number',)
    list_filter = ('updated_on', 'created_on')


@admin.register(BarberService)
class BarberServiceAdmin(admin.ModelAdmin):
    """
    Admin configuration for the BarberService model.
    Allows search by 'service_name' and displays 'service_name'
    and 'service_price' in the list view.
    Filters the list by 'updated_on' and 'created_on'.
    """
    search_fields = ['service_name']
    list_display = ('service_name', 'service_price',)
    list_filter = ('updated_on', 'created_on')


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Booking model.
    Allows search by 'user' and displays 'user', 'barber',
    'service', 'date', and 'time' in the list view.
    Filters the list by 'user', 'barber', 'service', 'date', and 'time'.
    """
    search_fields = ['user']
    list_display = ('user', 'barber', 'service', 'date', 'time')
    list_filter = ('user', 'barber', 'service', 'date', 'time')
