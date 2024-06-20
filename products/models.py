from django.core.validators import MinValueValidator
from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', null=True, blank=True)
    stock = models.IntegerField(default=5, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class FakeItem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
