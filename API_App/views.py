from django.shortcuts import render
from Blog.models import Post
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_home_page(request):
    all_posts = Post.objects.all() # A query set
    new_serialized_data = PostSerializers(all_posts, many=True)# Serializers converts one object at a time, in this case we have a more than one, hence many=True must be added
    return Response(new_serialized_data.data)

