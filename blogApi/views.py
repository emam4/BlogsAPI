from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"success": True})

@api_view(['GET'])
def get_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    except Post.DoesNotExist:
        response_message = {
                "success": False,
                "message": "Post not found"
        }
        return Response(response_message, status=404)


@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response_message = {
            "success": True,
            "message": "Post created successfully",
            "data": serializer.data
        }
        return Response(response_message, status=201)
    else:
        response_message = {
            "success": False,
            "errors": serializer.errors
        }
        return Response(response_message, status=400)
    
@api_view(['DELETE'])
def delete_post(request):
    post_id = request.data.get('post_id')
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            response_message = {
                "success": True,
                "message": "Post deleted successfully"
            }
            return Response(response_message, status=200)
        except Post.DoesNotExist:
            response_message = {
                "success": False,
                "message": "Post doesn't exist"
            }
            return Response(response_message, status=404)
        
@api_view(['PUT'])
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_message = {
                "success": True,
                "message": "Post updated successfully",
                "data": serializer.data
            }

            return Response(response_message, status=200)
    except:
        response_message = {
            "success": False,
            "message": "Error updating post"
        }
        return Response(response_message, status=400)