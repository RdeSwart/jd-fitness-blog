from . import views
from django.urls import path

#Add url pattern for BlogDetail view

urlpatterns= [
    path('', views.BlogDetail.as_view(), name='home'),
]