from django.contrib import admin
from .models import About, Collaboration, ContactUs
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on',)
    summernote_fields = ('content',)

# Registering the collaboration model.
@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('barber_name', 'barber_shop', 'email',)
    search_fields = ('barber_name', 'barber_shop',)
    list_filter = (
        'barber_name', 'barber_shop', 'created_on', 'service_offered',)
    readonly_fields = (
        'barber_name', 'barber_shop', 'business_type', 'service_offered', 'email', 'number', 'more_info',
    )


#Register the contact us model 
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'phone',)
    list_filter = ('name', 'created_on', 'is_finished',)
    list_display = ('name', 'email', 'is_finished',)
    readonly_fields = (
        'name', 'created_on', 'name', 'email', 'phone',)