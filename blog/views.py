from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View

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


class PostView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        form = CommentForm()

        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        context['form']= form

        return context


class CommentView(View):

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

            context['form'] = CommentForm()
            return render(request, 'blog/post-detail.html', context)

        context['form'] = form

        return render(request, 'blog/post-detail.html', context)
