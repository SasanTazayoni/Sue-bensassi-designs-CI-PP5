from django.urls import path
from . import views

urlpatterns = [
    path('', views.views_cart, name='view_cart'),
]