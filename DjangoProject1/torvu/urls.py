
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

    path('stay_informed/', views.stay_informed, name='stay_informed'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog_post', views.blog_post1, name='blog_post'),
    path('<slug:slug>/', views.blog_post, name='post'),
    path('tag/<slug:slug>/', views.blog_tag, name='tag'),
]
