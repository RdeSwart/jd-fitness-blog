from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.

#Allows you to CRUD blog posts from admin panel
admin.site.register(BlogPost)

#Allows you to approve comments and customises the data
admin.site.register(Comment)
