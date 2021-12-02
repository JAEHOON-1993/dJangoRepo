from rest_framework import serializers

from app.post.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta: #옵션 값
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'created',
            'updated',
        ]