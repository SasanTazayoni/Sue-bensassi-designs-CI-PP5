from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent', 'replied_to')
    list_filter = ('replied_to', 'date_sent')
    search_fields = ('name', 'email', 'message')
    ordering = ['date_sent']
