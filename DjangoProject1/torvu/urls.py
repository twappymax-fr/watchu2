
from torvu import views
from django.shortcuts import render
from django.urls import path

# Sitemap and Robots.txt
from django.contrib.sitemaps.views import sitemap
from torvu.sitemaps import *
from django.views.generic.base import TemplateView

# Create your views here.

app_name = 'torvu'



sitemaps = {
    'static': StaticSitemap,
    'posts': PostsSitemap,
}

urlpatterns = [

    path(
        'robots.txt/',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        )
    ),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', views.home, name='home'),
    path('form/', views.dummy_form, name='dummy_form'),

    path('request_assistance_form/', views.request_assistance_form, name='request_assistance_form'),

    path('success_page/', views.success_page, name='success_page'),

    path('stay_informed/', views.stay_informed, name='stay_informed'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog_post', views.blog_post1, name='blog_post'),
    path('blog/<slug:slug>/', views.blog_post, name='post'),
    path('tag/<slug:slug>/', views.blog_tag, name='tag'),
]
