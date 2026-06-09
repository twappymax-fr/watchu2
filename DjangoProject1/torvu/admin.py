from django.contrib import admin
from django.contrib.auth.models import User

from torvu.models import my_photos, RequestAssistanceModel

# Register your models here.

admin.site.register(my_photos)
admin.site.register(RequestAssistanceModel)