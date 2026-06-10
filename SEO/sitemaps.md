# Django Sitemaps

Sitemaps are dynamically generated XML files that give search engines a map of your website's structure, helping them index your pages more effectively.

Access your sitemap at: `yourdomain.com/sitemap.xml`

---

## 1. Enable the Sitemaps App

Add Django's built-in sitemap app to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.sitemaps',
]
```

---

## 2. Create `sitemaps.py`

Create a `sitemaps.py` file inside your main app folder (e.g. `post/sitemaps.py`):

```python
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Tag, Post


class StaticSitemap(Sitemap):
    """Lists static pages like home, about, etc."""

    def items(self):
        return ['home']  # Add other URL names e.g. 'about'

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    """Lists all category (tag) pages."""

    def items(self):
        return Tag.objects.all()


class PostPageSitemap(Sitemap):
    """Lists the latest 100 post pages."""

    def items(self):
        return Post.objects.all()[:100]
```

---

## 3. Add `get_absolute_url` to Models

Django needs to know the URL for each object. Add this method to your models in `models.py`:

### Tag model

```python
class Tag(models.Model):
    # ... existing fields ...

    def get_absolute_url(self):
        return f'/category/{self.slug}/'
```

### Post model

```python
class Post(models.Model):
    # ... existing fields ...

    def get_absolute_url(self):
        return f'/post/{self.id}/'
```

---

## 4. Register URLs

In your project's `urls.py`:

```python
# Sitemap configuration
from django.contrib.sitemaps.views import sitemap
from post.sitemaps import StaticSitemap, CategorySitemap, PostPageSitemap

sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap,
    'posts': PostPageSitemap,
}

urlpatterns = [
    # ...
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
```

---

## 5. Test

Run the development server and visit:

```
http://localhost:8000/sitemap.xml
```

You should see an XML list of all your indexed pages.

---

## Fix Domain in Database

If the sitemap shows the wrong domain (e.g. still `localhost` after deploying), update the **Sites** table in your database:

1. Go to Django Admin → Sites
2. Update the domain name to your live domain
3. Save — the sitemap will now show correct URLs

---

## Submitting to Google Search Console

Once deployed, submit your sitemap in Google Search Console:

1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Select your property
3. Click **Sitemaps** in the sidebar
4. Enter `sitemap.xml` and submit
