from django.urls import path
from .views import ListTodoList, DetailTodoList, CreateTodoList

app_name = 'todolist'

urlpatterns = [
    path('', ListTodoList.as_view(), name='list-todolist'),
    path('<int:pk>', DetailTodoList.as_view(), name='detail-todolist'),
    path('create/', CreateTodoList.as_view(), name='create-todolist'),
]
