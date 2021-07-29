from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost


# Create your views here.
class BlogView(ListView):
    model = BlogPost
    template_name = 'blog.html' 

    BlogView = get_object_or_404


