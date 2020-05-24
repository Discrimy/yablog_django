from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm, PostForm
from blog.models import Comment, Post


class IndexView(FormMixin, ListView):
    template_name = 'blog/index.html'
    paginate_by = 2
    model = Post

    form_class = PostForm


class PostView(FormMixin, DetailView):
    template_name = 'blog/post.html'
    model = Post

    form_class = CommentForm

    def get_initial(self):
        return {'post': self.kwargs['pk']}


class NewPostView(LoginRequiredMixin, FormView):
    template_name = 'blog/new_post.html'
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
