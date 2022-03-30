from django.contrib import admin
from blog.models import Blog, BlogImage
# Register your models here.

class ImageInline(admin.TabularInline):
    model = BlogImage


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author','title', 'created_at']
    list_filter = ['created_at']
    inlines = [ImageInline]