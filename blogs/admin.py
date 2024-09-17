from django.contrib import admin
from .models import Blogs

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp', 'new_slug')  # Include 'new_slug' in list_display if needed

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'timestamp', 'description', 'new_slug'),  # Ensure 'new_slug' is included here
        }),
    )
