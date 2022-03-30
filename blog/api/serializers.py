from blog.models import Blog, BlogImage
from rest_framework import serializers

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['image', 'created_at', 'modified_at']


class BlogSerializer(serializers.ModelSerializer):
    blog_image = BlogImageSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['user', 'title', 'content', 'slug', 'status', 'created_at', 'modified_at', 'blog_image']


