from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

# Blog Post Model
class BlogPost(models.Model):
    """
    post model allows superuser to write a blog post
    """
    blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_post")
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField("Category", related_name="posts")
    likes = models.ManyToManyField(User,related_name='blogpost_like', blank=True)
    featured_image = CloudinaryField('image', default='placeholder', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by: {self.blog_author}"

    def number_of_likes(self):
        return self.likes.count()

# Category Model
class Category(models.Model):
    """
    Category model allows blog posts to be put into categories
    """
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name


#Comments Model
class Comment(models.Model):
    """
    Comment model allows user to comment on a blog
    """
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Comment {self.post} by {self.author}"
