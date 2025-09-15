from rest_framework import serializers
from .models import Draft
from posts.serializers import PostSerializer


class DraftSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Draft
        fields = [
            "id",
            "author",
            "title",
            "content",
            "image",
            "created_at",
            "updated_at",
            "status",
            "published_at",
            "published_post",
            "is_owner",
        ]

    def get_is_owner(self, obj):
        request = self.context.get("request")
        return request.user == obj.author


class DraftDetailSerializer(DraftSerializer):
    published_post = PostSerializer(read_only=True)
