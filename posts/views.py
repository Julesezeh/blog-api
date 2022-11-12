from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer