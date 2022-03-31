from rest_framework import generics, permissions, authentication, response, parsers
from post.api.serializers import PostSerializer
from post.models import Post


class PostListCreateApiView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Post.objects.all().published()




PostListCreateApi = PostListCreateApiView.as_view()


class PostRetrieveDeleteApiView(generics.RetrieveDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Post.objects.all().published()
    lookup_field = 'slug'

PostRetrieveDeleteApi = PostRetrieveDeleteApiView.as_view()