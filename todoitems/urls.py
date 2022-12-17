from django.urls import path
from .views import ListTodoItems, UpdateTodoItem, CreateTodoItem, DeleteTodoItem


app_name = 'todoitems'

urlpatterns = [
    path('', ListTodoItems.as_view(), name='list-todoitems'),
    path('<int:pk>/update/', UpdateTodoItem.as_view(), name='update-todoitem'),
    path('create/', CreateTodoItem.as_view(), name='create-todoitem'),
    path('<int:pk>/delete/', DeleteTodoItem.as_view(), name='delete-todoitem'),
]
