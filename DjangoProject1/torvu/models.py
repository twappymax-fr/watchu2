from django.db import models

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