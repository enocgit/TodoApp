from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import TodoItemForm
from .models import TodoItem

# Create your views here.
class ListTodoItems(ListView):
    model = TodoItem
    template_name = 'todoitems/todoitems_list.html'
    context_object_name = 'todoitems'
    
class UpdateTodoItem(UpdateView):
    model = TodoItem
    template_name = 'todolist/todolist_update.html'
    context_object_name = 'todoitem'
    form_class = TodoItemForm
    # fields = ['task', 'completed']
    success_url = reverse_lazy('todolist:detail-todolist')
    
class CreateTodoItem(CreateView):
    model = TodoItem
    template_name = 'todoitems/todoitem_create.html'
    form_class = TodoItemForm
    # fields = ['task', 'completed', 'todolist']
    success_url = reverse_lazy('todolist:list-todolist')
    
    # def get_context_data(self, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      context['form']: TodoItemForm
    #      return context

class DeleteTodoItem(DeleteView):
    model = TodoItem
    template_name = 'todoitems/todoitem_delete.html'
    context_object_name = 'todoitem'
    success_url = reverse_lazy('todolist:list-todolist')
