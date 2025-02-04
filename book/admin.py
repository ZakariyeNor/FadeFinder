from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BookCover, Barber, BarberService, Booking


# Register your models here.
@admin.register(BookCover)
class BookCoverAdmin(SummernoteModelAdmin):
    summernote_fields = ('booking_intro',)

# For barbers.
@admin.register(Barber)
class BarberAdmin(SummernoteModelAdmin):
    search_fields = ['barber_name']
    list_display = ('barber_name', 'barber_address', 'barber_number',)
    list_filter = ('updated_on', 'created_on')


# For barbers'service.
@admin.register(BarberService)
class BarberServiceAdmin(SummernoteModelAdmin):
    search_fields = ['service_name']
    list_display = ('service_name', 'service_price',)
    list_filter = ('updated_on', 'created_on')

# For booking.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    search_fields = ['user']
    list_display = ('user', 'barber', 'service')