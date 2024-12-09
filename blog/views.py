from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BlogPost, Comment
from .forms import CommentForm

# Create your views here.
class BlogDetail(generic.ListView):
    """
    Renders Blog enteries in jumbotron view
    """
    queryset = BlogPost.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Renders the view for each blog post entry and its 
    content based on blogs slug.
    """

    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.order_by("-created_on")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment posted'
    )
    else:
        comment_form = CommentForm()
    

    return render(
        request,
        "blog/post_detail.html",
        {
        "post": post,
        "comments" : comments,
        "comment_count" : comment_count,
         "comment_form": comment_form,
         },
        
    )
