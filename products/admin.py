from django.contrib import admin
from .models import Product, Category, FakeItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class FakeItemAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FakeItem, FakeItemAdmin)
