from . import views
from django.urls import path, include
from django.contrib import admin

#Add url pattern for BlogDetail view

urlpatterns= [
    path('', views.BlogDetail.as_view(), name='home'),

    path('<slug:slug>/', views.post_detail, name='post_detail'),

    path('<slug:slug>/edit_comment/<int:comment_id>',
    views.comment_edit, name='comment_edit'),

    path('<slug:slug>/delete_comment/<int:comment_id>',
    views.comment_delete, name='comment_delete'),

    path("category/<category>/", views.blog_category, name='blog_category'),

    path('blogpost-like/<slug:slug>', views.BlogPostLike.as_view(), name='blogpost_like'),
]