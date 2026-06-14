from django.contrib import admin
from django.contrib.auth.models import User

from torvu.models import Post, PostBlock, Tag, my_photos, RequestAssistanceModel

# Register your models here.

admin.site.register(my_photos)
admin.site.register(RequestAssistanceModel)
admin.site.register(PostBlock)
admin.site.register(Post)
admin.site.register(Tag)