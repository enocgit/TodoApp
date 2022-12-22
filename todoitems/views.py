from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import TodoItemForm, TodoItemUpdateForm
from .models import TodoItem
from todolist.models import TodoList

# Create your views here.
class ListTodoItems(ListView):
    model = TodoItem
    template_name = 'todoitems/todoitems_list.html'
    context_object_name = 'todoitems'
    
class UpdateTodoItem(UpdateView):
    model = TodoItem
    template_name = 'todoitems/todoitem_update.html'
    context_object_name = 'todoitem'
    form_class = TodoItemUpdateForm
    # fields = ['task', 'completed']
    # success_url = reverse_lazy('todolist:list-todolist')
    
    def get_success_url(self):
        return reverse('todolist:detail-todolist', kwargs={'pk' : self.object.todolist.pk})
    
    
class CreateTodoItem(CreateView):
    model = TodoItem
    template_name = 'todoitems/todoitem_create.html'
    # form_class = TodoItemForm
    fields = ['task']
    context_object_name = 'todolist'
    # success_url = reverse_lazy('todolist:list-todolist')
    
    def get_success_url(self):
        return reverse('todolist:detail-todolist', kwargs={'pk': self.object.todolist.pk})
    
    def form_valid(self, form):
        todoitem = form.save()
        todolist = get_object_or_404(TodoList, pk=self.kwargs['pk'])
        todoitem.todolist = todolist
        todoitem.save()
        
        return redirect('todolist:detail-todolist', pk=todoitem.todolist.pk)
    #     # form.instance.todolist = self.request.POST['todolist']
    #     # todolist = TodoList.objects.get(pk=self.object.todolist.pk)
    #     # form.instance.todolist = todolist
    #     # form.save()
    #     # return super().form_valid(form)
    #     todoitem = form.save()
    #     todoitem.todolist = TodoList.objects.get()
    #     # form.instance.todolist = todolist
    #     # todolist.save()
    #     return redirect('todolist:list-todolist')
        # todoitem = form.save()
        # todolist = TodoItem.objects.get(pk=todoitem.todolist.pk)
        # todoitem.todolist = todolist

    
    # def get_context_data(self, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      context['form']: TodoItemForm
    #      return context

class DeleteTodoItem(DeleteView):
    model = TodoItem
    template_name = 'todoitems/todoitem_delete.html'
    context_object_name = 'todoitem'
    success_url = reverse_lazy('todolist:list-todolist')
    
    def get_success_url(self):
        return reverse('todolist:detail-todolist', kwargs={'pk': self.object.todolist.pk})
