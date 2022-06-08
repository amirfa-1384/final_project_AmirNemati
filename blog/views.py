from dataclasses import field
from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from .models import Post, Comment

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy,reverse

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

#_____________new_code____________

class ViewComment(CreateView):
    model = Comment
    template_name= 'Post_Comment.html'
    fields = ['post','comment','author']


class ViewDetilComment(DetailView):
    model = Comment
    context_object_name='comment'
    template_name = 'Comment_detail.html'

def ViewLike(request,pk):
    post =get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[int(pk)]))


