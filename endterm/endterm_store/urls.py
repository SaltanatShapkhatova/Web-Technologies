from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name = "blogs"),
    path('blogs/<int:blog_id>', views.blog_details, name = "blog_details"),
    path('add/', views.blog_add, name = "blog_add"),
    path('delete/<int:blog_id>/', views.blog_delete, name="blog_delete"),
    path('update/<int:blog_id>/', views.blog_update, name="blog_update"),
]