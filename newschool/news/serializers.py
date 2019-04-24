from rest_framework import serializers
from news.models import Post

# Post Serializer

#A serializer converts a Python/Django Model to a JSON (javascript)
#so we can use it in React


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'