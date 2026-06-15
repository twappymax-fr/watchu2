from django.contrib import admin

from torvu.models import Post, PostBlock, Tag, my_photos, RequestAssistanceModel


class PostBlockInline(admin.TabularInline):
    model = PostBlock
    fields = (
        'order',
        'block_type',
        'text',
        'cta_label',
        'cta_url',
        'image',
        'image_left',
        'image_right',
    )
    extra = 0
    ordering = ('order',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'created_at')
    list_filter = ('post_type',)
    search_fields = ('title', 'excerpt', 'author')
    inlines = [PostBlockInline]


class PostBlockAdmin(admin.ModelAdmin):
    list_display = ('post', 'order', 'block_type', 'cta_label')
    list_editable = ('order',)
    list_filter = ('post', 'block_type')
    search_fields = ('post__title', 'text', 'cta_label', 'cta_url')
    ordering = ('post', 'order')
    fieldsets = (
        (None, {
            'fields': ('post', 'order', 'block_type')
        }),
        ('Paragraph / Heading', {
            'fields': ('text',)
        }),
        ('CTA Button', {
            'fields': ('cta_label', 'cta_url')
        }),
        ('Blockquote', {
            'fields': ('quote_text', 'quote_attribution', 'quote_attributor_role')
        }),
        ('Image (single)', {
            'fields': ('image', 'image_alt', 'caption')
        }),
        ('Image Duo', {
            'fields': ('image_left', 'image_left_alt', 'image_right', 'image_right_alt', 'duo_caption')
        }),
        ('Pull Stat', {
            'fields': ('stat_number', 'stat_heading', 'stat_body')
        }),
    )


admin.site.register(my_photos)
admin.site.register(RequestAssistanceModel)
admin.site.register(PostBlock, PostBlockAdmin)
admin.site.register(Tag)