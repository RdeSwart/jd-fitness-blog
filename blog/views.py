from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPost

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

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )