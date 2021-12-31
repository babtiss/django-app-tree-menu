from django.views.generic import DetailView, ListView

from .models import Post


class AllPostView(ListView):
    template_name = 'post/all_posts.html'
    model = Post
    context_object_name = 'posts'


class PostView(DetailView):
    template_name = 'post/detail_post.html'
    model = Post
    context_object_name = 'post'
