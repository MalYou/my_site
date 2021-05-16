from django.shortcuts import get_object_or_404, render

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
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
        'tags': post.tags.all(),
    }
    return render(request, 'blog/post-detail.html', context)
