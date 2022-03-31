from rest_framework import generics, permissions, authentication, response, parsers, views
from post.api.serializers import PostSerializer, PostImageSerializer
from post.models import Post, Image
from django.utils.text import slugify

class PostListCreateApiView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Post.objects.all().published()
    # parser_classes = [parsers.FileUploadParser]

# class PostListCreateApiView(views.APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     authentication_classes = [authentication.TokenAuthentication]

#     def get(self, request, *args, **kwargs):
#         queryset = Post.objects.all().published()
#         serializer = PostSerializer(queryset, many=True)
#         return response.Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         images = request.data.pop("post_image")
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer['slug'] = slugify(serializer['title'])
#         post = serializer.save()
#         obj = Post.objects.get(slug=serializer['slug'])
#         for image in images:
#             Image.objects.create(post=obj, image=image)
#         return response.Response(post.data)


PostListCreateApi = PostListCreateApiView.as_view()





class PostRetrieveDeleteApiView(generics.RetrieveDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Post.objects.all().published()
    lookup_field = 'slug'

PostRetrieveDeleteApi = PostRetrieveDeleteApiView.as_view()