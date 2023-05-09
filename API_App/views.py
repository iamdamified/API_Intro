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


@api_view(["GET"])
def api_detail_page(request, id):
    single_post = Post.objects.get(id=id) # A query set
    serialized_post = PostSerializers(single_post)# Serializers converts one object at a time, in this case we have a more than one, hence many=True must be added
    return Response(serialized_post.data)


@api_view(["PUT"])
def api_update_page(request, id):
    single_post = Post.objects.get(id=id) # A query set
    new_data = request.data #collect new data and hold
    serialized_new_data = PostSerializers(single_post, data=new_data, partial=True)#
    if serialized_new_data.is_valid():
        serialized_new_data.save()
        return Response(serialized_new_data.data)
    else:
        return Response({"Error": "You typed rubbish!!"})
    

@api_view(["DELETE"])
def api_delete_page(request, id):
    single_post = Post.objects.get(id=id) # A query set
    single_post.delete() #delete
    return Response({"Success": "Post has been successfully deleted"})


@api_view(["POST"])
def api_create_page(request):
    new_data = PostSerializers(data=request.data)
    if new_data.is_valid():
        new_data.save()
        return Response(new_data.data)
