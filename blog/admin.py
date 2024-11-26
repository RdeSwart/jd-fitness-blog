from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.

#Allows you to CRUD blog posts from admin panel
admin.site.register(BlogPost)

#Allows you to approve comments and customises the data
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
