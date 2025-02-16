from django.contrib import admin
from .models import About, Collaboration
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.

    The AboutAdmin class customizes the admin interface for the About model, 
    including displaying the title and creation date and enabling Summernote 
    for content editing.
    """
    list_display = ('title', 'created_on',)
    summernote_fields = ('content',)


# Registering the collaboration model.
@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Collaboration model.

    The CollaborationAdmin class customizes the admin interface for the 
    Collaboration model, including search functionality, filtering options, 
    and setting specific fields as read-only.
    """
    list_display = (
        'barber_name', 'barber_shop', 'email',
    )
    search_fields = (
        'barber_name', 'barber_shop',
    )
    list_filter = (
        'barber_name', 'barber_shop',
        'created_on', 'service_offered',
    )
    readonly_fields = (
        'barber_name', 'barber_shop',
        'business_type', 'service_offered',
        'email', 'number', 'more_info',
    )
