
from torvu import views
from django.shortcuts import render
from django.urls import path

# Create your views here.

app_name = 'torvu'


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.dummy_form, name='dummy_form'),

    path('request_assistance_form/', views.request_assistance_form, name='request_assistance_form'),

    path('success_page/', views.success_page, name='success_page'),
]
