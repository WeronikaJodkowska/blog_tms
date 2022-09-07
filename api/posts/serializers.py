from rest_framework import serializers

from api.profiles.serializers import UserSerializer


class PostSerializer(serializers.Serializer):
    author = UserSerializer(read_only=True)
    title = serializers.CharField(max_length=200)
    image = serializers.ImageField(read_only=True)
    slug = serializers.SlugField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)