from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_form_view, name='contact')
]