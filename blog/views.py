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

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        form = CommentForm()
        tags = post.tags.all()
        context = {
            'post': post,
            'tags': tags,
            'form': form
        }

        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        context = {
            'post': post
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
