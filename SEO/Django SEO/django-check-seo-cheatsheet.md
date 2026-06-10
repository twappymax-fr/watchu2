# django-check-seo — Quick Reference

## Install

```bash
pip install django-check-seo
pip install djangocms
pip install packaging
```

## settings.py

```python
INSTALLED_APPS = [
    'django.contrib.sites',   # built-in
    'django_check_seo',
    'cms',
    'menus',
    'treebeard',
]

SITE_ID = 1
```

## urls.py

```python
from django.urls import path, include

urlpatterns = [
    path('django-check-seo/', include('django_check_seo.urls')),
]
```

## Migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

## Minimum Template Requirements

```html
<head>
    <title>Page Title</title>   <!-- required -->
</head>
<body>
    <h1>Main Heading</h1>       <!-- recommended -->
</body>
```

## Check a Page

| Page | URL |
|------|-----|
| Root `/` | `http://localhost:8000/django-check-seo/?page=/` |
| `/home/` | `http://localhost:8000/django-check-seo/?page=/home/` |
| `/about/` | `http://localhost:8000/django-check-seo/?page=/about/` |
| Any path | `http://localhost:8000/django-check-seo/?page=/your-path/` |
