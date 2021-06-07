from typing import List
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, View
from django.contrib import messages

from .models import Post
from .forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')

        return True if post_id in stored_posts else False

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        context = {
            'post': post,
            'tags': post.tags.all(),
            'comments': post.comments.all().order_by('-pk'),
            'form': CommentForm(),
            'is_stored_post':  self.is_stored_post(request, post.id)
        }

        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        context = {
            'post': post,
            'tags': post.tags.all(),
            'comments': post.comments.all().order_by('-pk'),
            'is_stored_post':  self.is_stored_post(request, post.id)
        }

        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.post = post
            comment_form.save()

            messages.success(request, 'Your comment is published!')

            return redirect('post_detail', slug=slug)

        context['form'] = form

        messages.error(request, 'Please correct your inputs!')
        return render(request, 'blog/post-detail.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        posts = []

        if stored_posts:
            posts = Post.objects.filter(id__in=stored_posts)

        context = {
            'posts': posts if posts else None
        }

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        post_id = int(request.POST['post_id'])

        if stored_posts is None:
            stored_posts = []

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session['stored_posts'] = stored_posts

        return redirect('read_later')
