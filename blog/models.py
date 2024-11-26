from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class BlogPost(models.Model):
    """
    post model
    """
    blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_post")
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by: {self.blog_author}"
