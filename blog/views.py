from django.shortcuts import render

from .models import Post

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    context = {
        'posts': latest_posts
    }
    return render(request, 'blog/index.html', context)

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/posts.html', context)

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
