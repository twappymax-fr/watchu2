# Check Your SEO with Django

This guide covers the `django-check-seo` package — a tool that audits the SEO of individual pages in your Django application and tells you exactly what to fix.

---

## Files

| File | Contents |
|------|----------|
| [django-check-seo.md](django-check-seo.md) | Full setup guide, usage, results interpretation, and troubleshooting |
| [django-check-seo-cheatsheet.md](django-check-seo-cheatsheet.md) | Quick-reference: install commands, settings, URL config, and checker URLs |

---

## TL;DR

1. `pip install django-check-seo djangocms packaging`
2. Add `django.contrib.sites`, `django_check_seo`, `cms`, `menus`, `treebeard` to `INSTALLED_APPS`
3. Set `SITE_ID = 1` in `settings.py`
4. Add `path('django-check-seo/', include('django_check_seo.urls'))` to `urls.py`
5. Run `python manage.py migrate`
6. Visit `http://localhost:8000/django-check-seo/?page=/your-path/`
