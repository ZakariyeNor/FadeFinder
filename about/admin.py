from django.contrib import admin
from .models import About, Collaboration
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
    prepopulated_fields = {
        'barber_shop': ('barber_name',)
    }

