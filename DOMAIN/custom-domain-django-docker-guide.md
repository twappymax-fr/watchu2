# Adding a Custom Domain to a Dockerized Django Application

This guide assumes:

- Django is running in Docker
- PostgreSQL is running in Docker
- Gunicorn is serving Django
- Nginx is acting as a reverse proxy
- You have a VPS with a public IP address
- You have purchased a domain name

---

# Architecture Overview

```text
Internet
    |
    v
Your Domain (example.com)
    |
    v
DNS Records
    |
    v
VPS Public IP
    |
    v
Nginx Container
    |
    v
Gunicorn Container
    |
    v
Django Application
    |
    v
PostgreSQL Container
```

---

# Step 1: Purchase a Domain

Buy a domain from any registrar:

- Namecheap
- Cloudflare Registrar
- Porkbun
- GoDaddy

Example:

```text
mywebsite.com
```

---

# Step 2: Find Your VPS Public IP

SSH into your VPS and run:

```bash
curl ifconfig.me
```

or

```bash
curl icanhazip.com
```

Example output:

```text
157.xxx.xxx.xxx
```

Save this IP address.

---

# Step 3: Configure DNS Records

Go to your domain registrar's DNS settings.

Create:

## Root Domain

```text
Type: A
Host: @
Value: YOUR_VPS_IP
TTL: Automatic
```

## WWW Domain

```text
Type: A
Host: www
Value: YOUR_VPS_IP
TTL: Automatic
```

Example:

```text
A     @      157.xxx.xxx.xxx
A     www    157.xxx.xxx.xxx
```

Wait for propagation.

Check with:

```bash
nslookup mywebsite.com
```

or

```bash
dig mywebsite.com
```

---

# Step 4: Update Django Settings

Open:

```python
settings.py
```

Update:

```python
ALLOWED_HOSTS = [
    "mywebsite.com",
    "www.mywebsite.com",
]
```

If using environment variables:

```python
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    ""
).split(",")
```

Example:

```env
ALLOWED_HOSTS=mywebsite.com,www.mywebsite.com
```

---

# Step 5: Update CSRF Trusted Origins

In settings.py:

```python
CSRF_TRUSTED_ORIGINS = [
    "https://mywebsite.com",
    "https://www.mywebsite.com",
]
```

or via environment variables:

```env
CSRF_TRUSTED_ORIGINS=https://mywebsite.com,https://www.mywebsite.com
```

---

# Step 6: Verify Nginx Configuration

Example nginx.conf:

```nginx
server {
    listen 80;

    server_name mywebsite.com www.mywebsite.com;

    location / {
        proxy_pass http://web:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }
}
```

Replace:

```text
mywebsite.com
```

with your actual domain.

---

# Step 7: Open Firewall Ports

Ubuntu UFW:

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw reload
```

Verify:

```bash
sudo ufw status
```

---

# Step 8: Deploy Updated Containers

Rebuild:

```bash
docker compose build
```

Restart:

```bash
docker compose up -d
```

Check:

```bash
docker ps
```

---

# Step 9: Verify HTTP Access

Open:

```text
http://mywebsite.com
```

If the site loads, DNS and Nginx are configured correctly.

Do NOT configure HTTPS until this step works.

---

# Step 10: Install Certbot

On Ubuntu:

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
```

Verify:

```bash
certbot --version
```

---

# Step 11: Obtain SSL Certificate

Run:

```bash
sudo certbot --nginx
```

Choose:

```text
mywebsite.com
www.mywebsite.com
```

Certbot will:

- Generate certificates
- Update Nginx
- Configure HTTPS redirects

---

# Step 12: Test HTTPS

Open:

```text
https://mywebsite.com
```

and

```text
https://www.mywebsite.com
```

You should see the lock icon.

---

# Step 13: Verify Auto-Renewal

Test:

```bash
sudo certbot renew --dry-run
```

If successful:

```text
Congratulations, all simulated renewals succeeded.
```

---

# Step 14: Update Environment Variables

Example production .env:

```env
DEBUG=False

SECRET_KEY=your-secret-key

ALLOWED_HOSTS=mywebsite.com,www.mywebsite.com

CSRF_TRUSTED_ORIGINS=https://mywebsite.com,https://www.mywebsite.com

POSTGRES_DB=my_database
POSTGRES_USER=my_user
POSTGRES_PASSWORD=my_password

DB_HOST=db
DB_PORT=5432
```

---

# Step 15: Final Checklist

- [ ] Domain purchased
- [ ] DNS A records configured
- [ ] Domain resolves to VPS IP
- [ ] ALLOWED_HOSTS updated
- [ ] CSRF_TRUSTED_ORIGINS updated
- [ ] Nginx server_name updated
- [ ] Firewall ports 80 and 443 open
- [ ] Docker containers rebuilt
- [ ] Site accessible via HTTP
- [ ] SSL certificate installed
- [ ] HTTPS working
- [ ] Auto-renewal verified

---

# Recommended Order

1. Buy domain
2. Point domain to VPS
3. Configure ALLOWED_HOSTS
4. Configure CSRF_TRUSTED_ORIGINS
5. Configure Nginx
6. Deploy containers
7. Verify HTTP works
8. Install SSL certificate
9. Verify HTTPS
10. Go live
