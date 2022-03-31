from post.models import Post, Image
from rest_framework import serializers
from django.utils.text import slugify


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'created_at', 'modified_at']


class PostSerializer(serializers.ModelSerializer):
    post_image = PostImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'title', 'content','category','slug', 'status', 'created_at', 'modified_at', 'post_image']
    
    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title']) 
        return super().create(validated_data)

