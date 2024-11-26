from django.contrib import admin
from .models import BlogPost

# Register your models here.

#Allows you to CRUD blog posts from admin panel
admin.site.register(BlogPost)
