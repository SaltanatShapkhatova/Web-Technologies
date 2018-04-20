from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name = "blogs"),
    path('blogs/<int:blog_id>', views.blog_list, name = "blog_details"),
    path('add/', views.blog_list, name = "blog_add"),
    path('delete/<int:blog_id>/', views.blog_detail, name="blog_delete"),
    path('update/<int:blog_id>/', views.blog_detail, name="blog_update"),
]