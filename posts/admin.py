from django.contrib import admin

# Register your models here.
from .models import post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['tags', 'slug']
    search_fields = ['title', 'contents']


admin.site.register(post, PostAdmin)
