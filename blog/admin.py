from django.contrib import admin
from .models import BlogPost, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

#Allows you to CRUD blog posts from admin panel
@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Using SummerNote, custom the admin config to manage
    BlogPost objects in the admin section of the site
    """
    list_display = ('title','slug','status')
    search_fields = ['title','content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

#Allows you to approve comments and customises the data
admin.site.register(Comment)
admin.site.register(Category)
