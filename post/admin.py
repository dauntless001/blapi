from django.contrib import admin
from post.models import Category, Post, Image
# Register your models here.

admin.site.register(Category)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title', 'created_at']
    list_filter = ['created_at']
    inlines = [ImageInline]