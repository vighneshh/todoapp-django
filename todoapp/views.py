from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView 
from .models import Post
from .forms import AddForm

class ToDoView(CreateView,ListView):
    model = Post
    form_class = AddForm
    template_name = 'todoapp/index.html'

def Completed(request, pk):
    post = Post.objects.get(pk=pk)
    post.completed = True
    post.save()
    return redirect('todo')

def DeleteCompleted(request):
    Post.objects.filter(completed__exact=True).delete()

    return redirect('todo')

def DeleteAll(request):
    Post.objects.all().delete()
    return redirect('todo')
