# Google Analytics & Google Search Console

Track your website's performance and understand how users find and interact with it.

---

## Google Analytics

Google Analytics is free and integrates seamlessly with other Google products. It tracks visitor behaviour, traffic sources, and engagement on your site.

### 1. Create an Account

1. Go to [analytics.google.com](https://analytics.google.com)
2. Click **Start measuring**
3. Fill in your **account name** (your company or brand)
4. Enter your **property name** (your website name)
5. Fill in business details and time zone/currency

### 2. Set Up a Data Stream

1. Add your website URL (e.g. `www.yourdomain.com`)
2. Enter a **stream name**
3. Click **Create stream**

### 3. Get Your Tracking Tag

1. Click **View tag instructions**
2. Select **Install manually**
3. Copy the Google tag snippet — it looks like this:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### 4. Add the Tag to `base.html`

Paste the snippet **immediately after the opening `<head>` tag**:

```html
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>

    <!-- rest of head -->
    <title>...</title>
</head>
```

### 5. Verify & Deploy

1. Deploy your updated code
2. Back in Google Analytics, click **Test**
3. Google will confirm it found the script on your page
4. Click **Next** — setup is complete

> Data collection takes approximately **2 days** to populate your dashboard.

---

## Google Search Console

Google Search Console (formerly Google Webmasters) shows how your website performs specifically on Google Search — impressions, clicks, average position, and which queries bring users to your site.

### 1. Add Your Property

1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Choose **URL prefix**
3. Enter your full website URL
4. If you already set up Google Analytics for this domain, you'll be **automatically verified**

### 2. Submit Your Sitemap

Help Google discover all your pages immediately:

1. In the left sidebar, click **Sitemaps**
2. Enter `sitemap.xml`
3. Click **Submit**

Google will now be aware of your sitemap and start crawling.

> Data collection takes **a day or so** before you see meaningful results.

### 3. What You Can Track

| Feature | Description |
|---------|-------------|
| Performance | Clicks, impressions, CTR, average position |
| URL Inspection | Check if a specific page is indexed |
| Sitemaps | Submit and monitor sitemap status |
| Coverage | See which pages are indexed or have errors |
| Core Web Vitals | Page experience signals (speed, layout shift) |

---

## Troubleshooting: Sitemap Domain Mismatch

If your sitemap shows the wrong domain (e.g. `localhost` or an old domain) after deploying:

1. Go to **Django Admin → Sites**
2. Find your entry in the Sites table
3. Update the **Domain name** to your live domain
4. Save the record
5. Re-check the sitemap — the URLs should now show the correct domain
6. Re-fetch in Google Search Console to get a success status
