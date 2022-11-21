from django.shortcuts import render
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post    # in template object_list or {nameModel}_list
    #context_object_name = 'all_posts'  # ila bghiti tbdl smya bach katrd 
    #ordering = ['-created_at']
    queryset = Post.objects.filter(active=False)





class PostDetail(DetailView):
    model = Post



