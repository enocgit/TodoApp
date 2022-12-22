from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, CreateView, DeleteView, View
from .models import TodoList
from todoitems.models import TodoItem
# from django.contrib.auth.models import User
from .forms import CreateListForm
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ListTodoList(LoginRequiredMixin, ListView):
    model = TodoList
    
    def get_context_data(self):
        context = super().get_context_data()
        context['todolists'] = TodoList.objects.filter(user=self.request.user)
        return context
    
    # model = TodoList
    # template_name = 'todolist/todolist_list.html'
    # context_object_name = 'todolists'
    
    # def get(self, request):
    #     if request.user.is_authenticated:
    #         detail_user_todolist = TodoList.objects.filter(user=request.user)
    #         return render(request, 'todolist/todolist_list.html', {'detail_user_todolist': detail_user_todolist})

    #     else:
    #         return render(request, 'todolist/todolist_list.html')
    
    # def get_queryset(self, request):
    #     if request.user:
    #         return TodoList.objects.filter(user=request.user)
    #     else:
    #         return TodoList.objects.all()
                
    
    # http_method_names = []
    
class DetailTodoList(LoginRequiredMixin, DetailView):
    model = TodoList
    template_name = 'todolist/todolist_detail.html'
    context_object_name = 'todolist'
    
class CreateTodoList(LoginRequiredMixin, CreateView):
    model = TodoList
    template_name = 'todolist/todolist_create.html'
    fields = ['name', 'icon_color']
    success_url = reverse_lazy('todolist:list-todolist')
    
    def form_valid(self, form):
        todolist = form.save()
        todolist.user = self.request.user
        todolist.save()
        # form.instance.user = self.request.user # associates request.user
        # return super().form_valid(form)        # to the active auth'd user
        return redirect('todolist:list-todolist')
    # model = TodoList
    # template_name = 'todolist/todolist_create.html'
    # fields = ['name', 'icon_color']
    # success_url = reverse_lazy('todolist:list-todolist')

    # def get(self, request):
    #     return render(request, 'todolist/todolist_create.html')
    
    # def post(self, request):
    #     # name = request.POST['name']
    #     # icon_color = request.POST['icon_color']
    #     # username = request.user.username
    #     # password = request.user.password
    #     # user = authenticate(request, username=username, password=password)
    #     # user = request.user
    #     # TodoList.objects.create(name=name, icon_color=icon_color)
    #     # todolist = TodoList(name=name, icon_color=icon_color)
    #     # todolist.user = request.user
    #     # todolist.save()
        
    #     form = CreateListForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('todolist:todolist_list')
    #     else:
    #         print(form)
    #         return render(request, 'todolist/todolist_create.html')
    #         # return reverse_lazy('accounts/login')
            
        
        # return reverse_lazy('todolist:list-todolist')
    
    
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         name = request.POST.get('todolist_todolist.name')
    #         icon_color = request.POST.get('icon_color')
    #         todolist = TodoList(name=name, icon_color=icon_color)
    #         todolist.save()
            
    #         return super().dispatch(request, *args, **kwargs)
    #     else:
    #         pass

class DeleteTodoList(LoginRequiredMixin, DeleteView):
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