from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterAdmin(admin.ModelAdmin):
    ordering = ('email',)


admin.site.register(NewsletterSubscription, NewsletterAdmin)
