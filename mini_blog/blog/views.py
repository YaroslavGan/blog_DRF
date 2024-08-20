from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerialaizer

# Create your views here.
class PostlistCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialaizer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    querity = Post.objects.all()
    serializer_class = PostSerialaizer

