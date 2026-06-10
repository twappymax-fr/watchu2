# Open Graph Meta Tags

Open Graph (OG) tags control how your pages look when shared on social media platforms like Facebook and Twitter/X. They populate the title, description, image and URL in social share cards.

Shared content creates **social signals** that indicate popularity and relevance to search engines, improving your ranking.

---

## 1. Add OG Tags to `base.html`

Place these inside the `<head>` section:

```html
<head>
    <!-- ... other meta tags ... -->

    <!-- The URL being shared -->
    <meta property="og:url" content="https://{{ request.META.HTTP_HOST }}{{ request.path }}">

    <!-- Page/post title -->
    <meta property="og:title" content="{% block og_caption %}Awesome{% endblock %}">

    <!-- Page/post description -->
    <meta property="og:description" content="{% block og_description %}Image sharing platform with rankings{% endblock %}">

    <!-- Content type -->
    <meta property="og:type" content="website">

    <!-- Share image (Facebook/LinkedIn) — 1200x630px recommended -->
    <meta property="og:image" content="https://{{ request.META.HTTP_HOST }}{% static 'images/awesome.jpeg' %}">

    <!-- Twitter/X card image — 600x600px (square) -->
    <meta name="twitter:image" content="https://{{ request.META.HTTP_HOST }}{% static 'images/awesome_tw.jpeg' %}">
</head>
```

> `{% block og_caption %}` and `{% block og_description %}` use Django template blocks so individual pages can override the default values.

---

## 2. Override OG Tags on Post Pages (`post_page.html`)

```html
{% block og_caption %}{{ post.body }}{% endblock %}

{% block og_description %}Shared by {{ post.author }} - {{ post.artist }}{% endblock %}

{% block og_image %}{{ post.image }}{% endblock %}

{% block tw_image %}{{ post.image }}{% endblock %}
```

Update `base.html` to also use blocks for the image tags:

```html
<meta property="og:image" content="{% block og_image %}https://{{ request.META.HTTP_HOST }}{% static 'images/awesome.jpeg' %}{% endblock %}">
<meta name="twitter:image" content="{% block tw_image %}https://{{ request.META.HTTP_HOST }}{% static 'images/awesome_tw.jpeg' %}{% endblock %}">
```

---

## 3. Prepare Share Images

Create two images and place them in `static/images/`:

| File | Size | Platform |
|------|------|----------|
| `awesome.jpeg` | 1200 × 630 px | Facebook, LinkedIn |
| `awesome_tw.jpeg` | 600 × 600 px | Twitter/X |

After adding static files, run:

```bash
python manage.py collectstatic
```

---

## 4. Test with Facebook Debugger

After deploying, verify your OG tags at:

```
https://developers.facebook.com/tools/debug
```

1. Paste your URL
2. Click **Debug**
3. Click **Fetch new information**
4. Check the preview — title, description and image should all appear correctly

### Common warnings from Facebook Debugger

| Warning | Fix |
|---------|-----|
| Missing `og:type` | Add `<meta property="og:type" content="website">` |
| Missing `fb:app_id` | Optional — only needed for Facebook Insights/analytics |

---

## 5. Complete OG Tag Reference

```html
<meta property="og:url"         content="...">  <!-- Canonical URL -->
<meta property="og:title"       content="...">  <!-- Title of the page/post -->
<meta property="og:description" content="...">  <!-- Brief summary -->
<meta property="og:image"       content="...">  <!-- Preview image URL -->
<meta property="og:type"        content="website">  <!-- website, article, video, etc. -->
<meta name="twitter:image"      content="...">  <!-- Square image for Twitter/X -->
```
