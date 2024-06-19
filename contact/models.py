from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)
    replied_to = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_sent']

    def __str__(self):
        return f"Enquiry from {self.name} ({self.email})"
