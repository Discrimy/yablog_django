from django.urls import path

from blog.views import IndexView, NewCommentView, NewPostView, PostView

urlpatterns = [
    path('posts', IndexView.as_view(), name='blog-index'),
    path('posts/<int:pk>', PostView.as_view(), name='blog-post'),
    path('posts/new', NewPostView.as_view(), name='blog-new-post'),
    path('comment/new', NewCommentView.as_view(), name='blog-new-comment'),
]
