from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    template_name = 'index.html'
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 3

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approve=True).order_by('-created_on')
        return render(
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments
            },
        )