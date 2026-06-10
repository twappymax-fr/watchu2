# django-check-seo: Audit Your Django App's SEO

`django-check-seo` is a package that analyses each page of your Django application and reports what SEO is good, what's missing, and what can be improved — per URL.

---

## What It Does

- Checks every individual page/route in your Django app
- Identifies SEO problems (errors) and warnings
- Gives descriptions and suggestions for each issue found
- Confirms what's working correctly

---

## Requirements

Before running checks, each page being tested **must** have:

- A `<title>` tag — **required**, the checker will error without it
- At least one `<h1>` tag — recommended best practice

---

## Setup Guide

### Step 1 — Install the package

```bash
pip install django-check-seo
```

This installs several sub-packages automatically. That's expected behaviour.

---

### Step 2 — Install dependencies

The checker depends on **Django CMS** and **Packaging**:

```bash
pip install djangocms
pip install packaging
```

---

### Step 3 — Update `INSTALLED_APPS` in `settings.py`

Add the following apps:

```python
INSTALLED_APPS = [
    # ... your existing apps ...

    'django.contrib.sites',   # required — built-in, no install needed
    'django_check_seo',
    'cms',
    'menus',
    'treebeard',
]
```

Also ensure `SITE_ID` is set (uncomment if it's already there):

```python
SITE_ID = 1
```

---

### Step 4 — Add the URL to `urls.py`

In your **main project** `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ... existing URLs ...
    path('django-check-seo/', include('django_check_seo.urls')),
]
```

---

### Step 5 — Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 6 — Prepare your template

Make sure the page you're testing has at minimum:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Hello World</h1>
    <h2>A subheading</h2>
</body>
</html>
```

---

## Running the SEO Checker

### Check the root/homepage (`/`)

```
http://localhost:8000/django-check-seo/?page=/
```

### Check a named route (e.g. `/home/`)

```
http://localhost:8000/django-check-seo/?page=/home/
```

### Check any other page

```
http://localhost:8000/django-check-seo/?page=/your-path/
```

The `page=` query parameter takes the **URL path** of the page you want to audit.

---

## Reading the Results

The checker output is divided into three sections:

| Section | Meaning |
|---------|---------|
| ✅ **Checks found** | SEO elements present and correct |
| ⚠️ **Warnings** | Present but could be improved |
| ❌ **Problems** | Missing or broken SEO elements |

### Example workflow

1. Run the checker on a page
2. See a warning: *"No H2 tag found"*
3. Add `<h2>` to your template, refresh
4. Warning clears — checker now shows H2 tags found
5. New suggestion appears: *"No keyword found"* — add keywords and repeat

---

## Troubleshooting

### RuntimeError on startup

**Cause:** `django.contrib.sites` is missing from `INSTALLED_APPS` or `SITE_ID` is not set.

**Fix:**
```python
# settings.py
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
]

SITE_ID = 1
```

### Checker returns an error on the page

**Cause:** The page being tested has no `<title>` tag.

**Fix:** Add a `<title>` to the template's `<head>` section.

### `page not found` on root URL after switching to a named route

This is expected. If you changed your URL from `''` to `'home/'`, the root path no longer exists. Use `?page=/home/` instead of `?page=/`.
