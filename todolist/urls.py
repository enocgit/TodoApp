from django.urls import path
from .views import ListTodoList, DetailTodoList, CreateTodoList, DeleteTodoList
from todoitems.views import CreateTodoItem

app_name = 'todolist'

urlpatterns = [
    path('', ListTodoList.as_view(), name='list-todolist'),
    path('<int:pk>', DetailTodoList.as_view(), name='detail-todolist'),
    path('create/', CreateTodoList.as_view(), name='create-todolist'),
    path('<int:pk>/todoitems/create', CreateTodoItem.as_view(), name='create-todoitem'),
    # path('<int:pk>/todoitems/', CreateTodoItem.as_view(), name='create-todoitem'),
    path('<int:pk>/delete', DeleteTodoList.as_view(), name='delete-todolist'),
]
