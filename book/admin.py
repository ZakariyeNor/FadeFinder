from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BookCover


# Register your models here.
@admin.register(BookCover)
class BookCoverAdmin(SummernoteModelAdmin):
    summernote_fields = ('booking_intro',)