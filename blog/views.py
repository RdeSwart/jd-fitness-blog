from django.shortcuts import render
from django.views import generic
from .models import BlogPost

# Create your views here.
class BlogDetail(generic.ListView):
    queryset = BlogPost.objects.all()
    template_name = "blogpost_list.html"