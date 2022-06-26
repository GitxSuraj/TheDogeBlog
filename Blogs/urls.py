from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.posts, name='blog'),
    path("blog/blog_post=<int:blog_id>/topic=<str:blog_title>", views.blogView, name="blogView"),   
]