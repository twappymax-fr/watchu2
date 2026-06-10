# robots.txt

The `robots.txt` file tells web crawlers (search engine bots) which pages they should **not** index. It's a standard that all major search engines respect.

Access it at: `yourdomain.com/robots.txt`

---

## 1. Create the File

Create `robots.txt` inside your `templates/` folder:

```
User-agent: *
Disallow: /admin/
Disallow: /another-private-path/
```

- **`User-agent: *`** — applies the rules to all web crawlers
- **`Disallow:`** — each line blocks a path from being indexed
- Add a new `Disallow:` line for each additional path you want to block

---

## 2. Register the URL

In `urls.py`, use Django's `TemplateView` to serve the file as a plain-text response — no need for a separate view function:

```python
from django.views.generic.base import TemplateView

urlpatterns = [
    # ...
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        )
    ),
]
```

---

## 3. Test

Start the server and visit:

```
http://localhost:8000/robots.txt
```

You should see the plain-text content of your `robots.txt` file.

---

## Notes

- The `robots.txt` is a suggestion, not a hard block — malicious bots may ignore it.
- For truly private pages (e.g. admin), also ensure proper authentication is in place.
- You can use `Allow:` to explicitly permit paths under a broader `Disallow:`.
