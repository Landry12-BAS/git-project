# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.page_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('service/', views.services_view, name='services'),
    path('contact/', views.contact_view, name='contact'),
]
