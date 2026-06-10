# Django Deployment — Part 12: SEO, Sitemaps, Open Graph & Google Analytics

> Tutorial by **Andreas** — Tech-curious web designer  
> Part of a Django deployment series

---

## Overview

This tutorial covers making a Django website production-ready with full SEO optimization. By the end, the site will be discoverable by search engines and share-ready on social media.

---

## Topics Covered

| # | Topic | File |
|---|-------|------|
| 1 | Sitemaps | [sitemaps.md](./sitemaps.md) |
| 2 | robots.txt | [robots-txt.md](./robots-txt.md) |
| 3 | Page Titles, Alt Text & Meta Tags | [meta-tags.md](./meta-tags.md) |
| 4 | Open Graph Meta Tags | [open-graph.md](./open-graph.md) |
| 5 | Google Analytics & Search Console | [analytics.md](./analytics.md) |

---

## Quick Summary

### On-Site SEO Strategies
- **Sitemaps** — XML file that tells search engines about your site structure
- **robots.txt** — Controls which pages search engines should NOT index
- **Page titles** — Unique, descriptive titles per page improve rankings
- **Alt text** — Describes images for accessibility and image search
- **H1 headings** — Define the main topic with relevant keywords
- **Meta tags** — Description, keywords and author shown in search results
- **Open Graph tags** — Controls how content appears when shared on social media

### Off-Site SEO Strategies
- **Google Ads** — Drive traffic and improve visibility
- **Google Reviews** — Build trust and increase click-through rate
- **Backlinks** — Articles linking to your site signal relevance to search engines

---

## Prerequisites

- Django project with a working app (examples use a `post` app)
- Models: `Post` and `Tag`
- Templates: `base.html`, `post_page.html`, `profile.html`, `inbox.html`, `header.html`
- Static files configured
