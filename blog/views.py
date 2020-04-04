from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment


class IndexView(FormMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    form_class = PostForm

    def get_queryset(self):
        return Post.objects.all()


class PostView(FormMixin, DetailView):
    template_name = 'blog/post.html'
    model = Post

    form_class = CommentForm

    def get_initial(self):
        return {'post': self.kwargs['pk']}


class NewPostView(LoginRequiredMixin, FormView):
    form_class = PostForm

    def form_valid(self, form):
        post = Post(
            title=form.cleaned_data['title'],
            content=form.cleaned_data['content'],
            author=self.request.user,
        )
        post.save()
        return redirect(reverse('blog-post', kwargs={'pk': post.id}))


class NewCommentView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = Comment(
            content=form.cleaned_data['content'],
            post=get_object_or_404(Post, pk=form.cleaned_data['post']),
            author=self.request.user,
        )
        comment.save()
        return redirect(reverse('blog-post', kwargs={'pk': comment.post.id}))
