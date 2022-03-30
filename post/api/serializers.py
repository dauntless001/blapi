from post.models import Post, Image
from rest_framework import serializers

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'created_at', 'modified_at']


class PostSerializer(serializers.ModelSerializer):
    post_image = PostImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'slug','category', 'status', 'created_at', 'modified_at', 'post_image']


