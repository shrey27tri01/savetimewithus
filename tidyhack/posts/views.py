from django.shortcuts import render

# Create your views here.

from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from datetime import date



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def seeOthers(request):
    today = date.today()
    posts = Post.objects.all().filter(created_at__day=today.day,created_at__month=today.month,created_at__year=today.year)
    context = {"posts":posts}
    return render(request,"posts/seeOthers.html",context)