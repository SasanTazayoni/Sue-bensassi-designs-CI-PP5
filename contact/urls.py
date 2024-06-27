from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
    path('edit/<int:enquiry_id>/',
         views.edit_enquiry, name='edit_enquiry'),
    path('delete/<int:enquiry_id>/',
         views.delete_enquiry, name='delete_enquiry'),
]
