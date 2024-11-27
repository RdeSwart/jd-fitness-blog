from . import views
from django.urls import path

#Add url pattern for BlogDetail view

urlpatterns= [
    path('', views.BlogDetail.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]