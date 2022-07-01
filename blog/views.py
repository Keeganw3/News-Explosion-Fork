from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, SocialMediaPlatform
from .forms import CommentForm


class PostList(generic.ListView):
    template_name = 'index.html'
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 3


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        return render(
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
                "left_comment": False
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')

        make_comment = CommentForm(data=request.POST)

        if make_comment.is_valid():
            make_comment.instance.email = request.user.email
            make_comment.instance.name = request.user.username
            comment = make_comment.save(commit=False)
            comment.post = post
            comment.save()
        else:
            make_comment = CommentForm()

        return render(
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
                "left_comment": True
            },
        )

# def social_media_base_view(request):
#     smbase = SocialMediaPlatform.objects.all()
#     context['smbase'] = smbase

#     return render('request', 'templates/base.html', context)