from rest_framework import generics, permissions, authentication
from blog.api.serializers import BlogSerializer
from blog.models import Blog


class BlogListCreateApiView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Blog.objects.all().published()


BlogListCreateApi = BlogListCreateApiView.as_view()


class BlogRetrieveDeleteApiView(generics.RetrieveDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Blog.objects.all().published()
    lookup_field = 'slug'

BlogRetrieveDeleteApi = BlogRetrieveDeleteApiView.as_view()