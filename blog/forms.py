from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class to create and update Comments on 
    blog posts
    """
    class Meta:
        model = Comment
        fields = ('body',)