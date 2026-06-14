from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import my_photos, Post, Tag


class StaticSitemap(Sitemap):
    def items(self):
        return ['torvu:home', 'torvu:about', 'torvu:contact', 'torvu:request_assistance_form',
                'torvu:stay_informed', 'torvu:contact']

    def location(self, item):
        return reverse(item)

class PhotosSitemap(Sitemap):
    def items(self):
        return my_photos.objects.all()


class PostsSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

class TagsSitemap(Sitemap):
    def items(self):
        return Tag.objects.all()
