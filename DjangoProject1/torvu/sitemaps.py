from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import my_photos


class StaticSitemap(Sitemap):
    def items(self):
        return ['torvu:home']

    def location(self, item):
        return reverse(item)

class PhotosSitemap(Sitemap):
    def items(self):
        return my_photos.objects.all()