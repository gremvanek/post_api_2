from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "image",
            "author",
            "date_created",
            "date_modified",
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = ["id", "author", "text", "post", "date_created", "date_modified"]
