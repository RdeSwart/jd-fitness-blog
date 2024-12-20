from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
from .models import BlogPost, Comment, Category
from .forms import CommentForm

# Overview list of blogs View
class BlogDetail(generic.ListView):
    """
    Renders Blog enteries in jumbotron view
    """
    queryset = BlogPost.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6


# Category View
def blog_category(request, category):
    """
    Renders Blog list in certain Categories
    """
    posts = BlogPost.objects.filter(
    categories__name__contains=category
    ).order_by("-created_on")
    print(f"Posts in category '{category}': {[post.title for post in posts]}")  # Debug statement
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)



# Full blog content View
def post_detail(request, slug):
    """
    Renders the view for each blog post entry and its 
    content based on blogs slug.
    Displays any comments related to this blog post.
    Displays likes and if user has liked already.
    """

    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.order_by("-created_on")
    comment_count = post.comments.count()
    like = False

    if post.likes.filter(id=request.user.id).exists():
        like=True

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
         "liked": like,
         },
        
    )


# Edit Comment View
def comment_edit(request, slug, comment_id):
    """
    Login required to edit comments
    """
    if request.method == "POST":

        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated Successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Delete Comment View
def comment_delete(request, slug, comment_id):
    """
    Login required to delete users own comment only
    """
    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Likes View
class BlogPostLike(View):
    """
    Allows user to like or unlike a blog post
    """
    def post(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))