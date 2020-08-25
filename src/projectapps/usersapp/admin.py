from django.contrib import admin
from .models import Incident, Post, State
from django.utils.text import slugify

# Register your models here.
admin.site.register(Incident)
admin.site.register(State)

class PostAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('content',)}
    def slugify_max(self, text, max_length=50):
        slug = slugify(text)
        if len(slug) <= max_length:
            return slug
        trimmed_slug = slug[:max_length].rsplit('-', 1)[0]
        if len(trimmed_slug) <= max_length:
            return trimmed_slug
        # First word is > max_length chars, so we have to break it
        return slug[:max_length]
    
admin.site.register(Post, PostAdmin)