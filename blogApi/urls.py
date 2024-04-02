from django.urls import include, path
from .views import get_post, get_all_posts, create_post, update_post, delete_post

urlpatterns = [
    path('get-post/<int:post_id>', get_post),
    path('get-posts', get_all_posts),
    path('create-post', create_post),
    path('update-post/<int:post_id>', update_post),
    path('delete-post', delete_post),
]