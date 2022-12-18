from django.urls import path
from .views import ListTodoList, DetailTodoList, CreateTodoList, DeleteTodoList

app_name = 'todolist'

urlpatterns = [
    path('', ListTodoList.as_view(), name='list-todolist'),
    path('<int:pk>', DetailTodoList.as_view(), name='detail-todolist'),
    path('create/', CreateTodoList.as_view(), name='create-todolist'),
    path('<int:pk>/delete', DeleteTodoList.as_view(), name='delete-todolist'),
]
