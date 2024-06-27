from django.db import models
from profiles.models import UserProfile


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)
    replied_to = models.BooleanField(default=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='enquiries'
    )

    class Meta:
        verbose_name_plural = 'Enquiries'
        ordering = ['date_sent']

    def __str__(self):
        return f"Enquiry from {self.name} ({self.email})"
