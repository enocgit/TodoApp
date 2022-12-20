from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import TodoList
from todoitems.models import TodoItem
from django.contrib.auth.models import User

# Create your views here.
class ListTodoList(ListView):
    model = TodoList
    template_name = 'todolist/todolist_list.html'
    context_object_name = 'todolists'
    
    
    # http_method_names = []
    
class DetailTodoList(DetailView):
    model = TodoList
    template_name = 'todolist/todolist_detail.html'
    context_object_name = 'todolist'
    
class CreateTodoList(CreateView):
    model = TodoList
    template_name = 'todolist/todolist_create.html'
    fields = ['name', 'icon_color']
    success_url = reverse_lazy('todolist:list-todolist')
    
    

class DeleteTodoList(DeleteView):
    model = TodoList
    template_name = 'todolist/todolist_delete.html'
    context_object_name = 'todolist'
    success_url = reverse_lazy('todolist:list-todolist')


# class UpdateTodoList(UpdateView):
#     model = TodoItem
#     template_name = 'todolist/todolist_update.html'
#     context_object_name = 'todolist'
#     fields = ['task', 'completed']
#     success_url = reverse_lazy('todolist:list-todolist')