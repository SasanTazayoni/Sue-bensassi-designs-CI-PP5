from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    ordering = ('email',)


admin.site.register(Newsletter, NewsletterAdmin)
