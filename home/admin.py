from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BarberInfo, ServicesDes

# Register your models here.
@admin.register(BarberInfo)
class BarberInfoAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    search_fields = ('title',)
    summernote_fields = ('description',)


@admin.register(ServicesDes)
class ServicesDesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    search_fields = ('title',)
    summernote_fields = ('description',)