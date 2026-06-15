from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class my_photos(models.Model):
    photo_name = models.CharField(max_length=100)
    photo_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo_name


class RequestAssistanceModel(models.Model):

    # ── STEP 1: CONTACT INFORMATION ──────────────────────────────────────────

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal = models.CharField(max_length=20)

    gender = models.CharField(max_length=20)

    # ── STEP 2: EDUCATION ────────────────────────────────────────────────────

    edu_level = models.CharField(max_length=100)
    edu_major = models.CharField(max_length=150, blank=True)

    edu_grad_year = models.PositiveIntegerField()

    edu_institution = models.CharField(max_length=200)
    edu_inst_location = models.CharField(max_length=150)

    edu_certs = models.TextField(blank=True)

    # ── STEP 3: EMPLOYMENT ───────────────────────────────────────────────────

    emp_status = models.CharField(max_length=100)

    emp_title = models.CharField(max_length=150)
    emp_employer = models.CharField(max_length=200)
    emp_address = models.CharField(max_length=255)

    emp_start = models.DateField()
    emp_end = models.DateField(null=True, blank=True)

    emp_ssn = models.CharField(max_length=11)
    emp_ssn_confirm = models.CharField(max_length=11)

    upload_w4 = models.FileField(
        upload_to='uploads/w4/'
    )

    upload_i9 = models.FileField(
        upload_to='uploads/i9/'
    )

    emp_summary = models.TextField()

    # ── STEP 4: IDENTITY VERIFICATION ────────────────────────────────────────

    id_type = models.CharField(max_length=100)
    id_number = models.CharField(max_length=50)

    id_state = models.CharField(max_length=100)

    id_issue = models.DateField()
    id_expiry = models.DateField()

    id_upload_front = models.FileField(
        upload_to='uploads/id/front/'
    )

    id_upload_back = models.FileField(
        upload_to='uploads/id/back/'
    )

    id_upload_selfie = models.FileField(
        upload_to='uploads/id/selfie/'
    )

    terms_agree = models.BooleanField(default=False)

    # ── METADATA ─────────────────────────────────────────────────────────────

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Request Assistance Form"
        verbose_name_plural = "Request Assistance Forms"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.email}"


# models.py




class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/tag/{self.slug}/'


class Post(models.Model):


    class Post_Type(models.TextChoices):
        NEWS     = 'news',     'News'
        GUIDE = 'guide', 'Guide'
        GOOD_FEED = 'good_feed', 'Good Feed'
        TESTIMONIAL = 'testimonial', 'Testimonial'

    # Core identity
    title = models.CharField(max_length=10000)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    category = models.CharField(max_length=500)          # e.g. "Climate & Livelihoods"
    tags        = models.ManyToManyField(Tag, blank=True, related_name='posts')
    post_type = models.CharField(max_length=20, choices=Post_Type.choices)  # e.g. "News", "Guide", "Good Feed", "Testimonial"

    # Authorship
    author      = models.CharField(max_length=500)
    author_role = models.CharField(max_length=500, blank=True)  # e.g. "Field Correspondent, Torvu Tanzania"

    # Hero
    hero_image  = models.ImageField(upload_to='blog/heroes/', blank=True, null=True)
    hero_alt    = models.CharField(max_length=255, blank=True)

    # Body — stored as an ordered list of content blocks (see PostBlock below)

    # Meta / SEO
    excerpt     = models.TextField(max_length=6000, blank=True)  # used in story cards
    read_time   = models.PositiveSmallIntegerField(default=5)   # minutes

    # Lifecycle
    created_at  = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'



class PostBlock(models.Model):
    """
    One ordered content block within a post.
    Each row is one discrete piece of content — paragraph, heading,
    blockquote, image, pull-stat, or image duo.
    The template iterates over these in `order` to build the article body.
    """

    class BlockType(models.TextChoices):
        PARAGRAPH  = 'paragraph',   'Paragraph'
        HEADING    = 'heading',     'Heading (h3)'
        BLOCKQUOTE = 'blockquote',  'Blockquote'
        IMAGE      = 'image',       'Image'
        IMAGE_DUO  = 'image_duo',   'Image Duo (2-up)'
        PULL_STAT  = 'pull_stat',   'Pull Stat'

    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='blocks')
    order      = models.PositiveSmallIntegerField()
    block_type = models.CharField(max_length=2000, choices=BlockType.choices)

    # --- PARAGRAPH / HEADING ---
    # Supports inline <strong> via a safe HTML subset; or swap for a plain
    # TextField and run a markdown renderer in the template.
    text       = models.TextField(blank=True)

    # --- BLOCKQUOTE ---
    quote_text = models.CharField(max_length=10000, blank=True)  # "Amara Mwalimu"
    quote_attribution = models.CharField(max_length=15000, blank=True)
    quote_attributor_role = models.CharField(max_length=15000, blank=True)

    # --- IMAGE (single) ---
    image      = models.ImageField(upload_to='blog/blocks/', blank=True, null=True)
    image_alt  = models.CharField(max_length=5050, blank=True)
    caption    = models.CharField(max_length=4000, blank=True)

    # --- IMAGE DUO ---
    image_left       = models.ImageField(upload_to='blog/blocks/', blank=True, null=True)
    image_left_alt   = models.CharField(max_length=25500, blank=True)
    image_right      = models.ImageField(upload_to='blog/blocks/', blank=True, null=True)
    image_right_alt  = models.CharField(max_length=25500, blank=True)
    duo_caption      = models.CharField(max_length=40000, blank=True)

    # --- PULL STAT ---
    stat_number  = models.CharField(max_length=30000, blank=True)   # e.g. "3×", "41%"
    stat_heading = models.CharField(max_length=20000, blank=True)
    stat_body    = models.TextField(blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.post.title} — block {self.order} ({self.block_type})'