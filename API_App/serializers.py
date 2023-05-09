from rest_framework import serializers
from Blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "date_posted"]# NOTE: 


        fields = "__all__"