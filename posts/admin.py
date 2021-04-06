#Django
from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    list_display = ('pk', 'title', 'user', 'photo')
    search_fields = ('user',)
    list_editable = ('photo',)
    list_filter = ('created', 'title', 'user')
