# Page Titles, Alt Text & Meta Tags

These on-page SEO elements help search engines understand your content and improve your rankings.

---

## 1. Dynamic Page Titles

Give each page its own `<title>` by using Django template blocks.

### `base.html`

```html
<head>
    <title>{% block title %}{% endblock %} | Awesome</title>
</head>
```

### Static page (e.g. `create_post.html`)

```html
{% block title %}Create Post{% endblock %}
```

### Dynamic page — user profile (`profile.html`)

```html
{% block title %}{{ profile.user.username }}{% endblock %}
```

### Dynamic page — post detail (`post_page.html`)

```html
{% block title %}{{ post.title }}{% endblock %}
```

**Result:** Browser tabs and search engine results will show unique, descriptive titles like:
- `Create Post | Awesome`
- `john_doe | Awesome`
- `Beautiful Sunset | Awesome`

---

## 2. Image Alt Text

Alt text describes images for screen readers and image search indexing. Always add it to `<img>` tags.

### Logo in `header.html`

```html
<img src="{% static 'images/logo.png' %}" alt="Awesome">
```

> Use your brand name as the alt text for your logo.

### Post images

```html
<img src="{{ post.image }}" alt="{{ post.caption }}">
```

---

## 3. HTML Meta Tags

Add these to the `<head>` section of `base.html`, below the `<title>`:

```html
<head>
    <title>{% block title %}{% endblock %} | Awesome</title>

    <!-- Page description shown in search results -->
    <meta name="description" content="Image sharing platform with rankings">

    <!-- Relevant keywords for your site -->
    <meta name="keywords" content="photography, images, flickr, rankings, sharing">

    <!-- Author / brand name -->
    <meta name="author" content="Awesome">
</head>
```

### Meta tag purposes

| Tag | Purpose | SEO Impact |
|-----|---------|------------|
| `description` | Short summary shown under the link in search results | Improves click-through rate |
| `keywords` | Relevant terms for your content | Minor direct ranking impact |
| `author` | Identifies the content creator or brand | Useful for article/blog content |

---

## Tips

- Keep descriptions under **160 characters** so they don't get cut off in search results.
- Write descriptions that are compelling — they act like ad copy in search results.
- Keywords should be natural terms your audience would actually search for.
