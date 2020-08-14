
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Category
from .permissions import IsPostAuthor
from .serializers import PostSerializer, CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailsView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class PostsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailsView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        # post.author = request.user
        # post.save()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdatePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthor, ]


class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthor, ]




# TODO: Viewsets
# TODO: Pagination
# TODO: Search(F(), Q())
# TODO: Filtering
