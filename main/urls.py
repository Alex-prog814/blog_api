from django.urls import path

from main.views import *

urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('posts/create/', CreatePostView.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', UpdatePostView.as_view(), name='update-post'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('category/<slug:slug>/', CategoryDetailsView.as_view(), name='category-details'),
]