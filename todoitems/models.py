from django.db import models
from todolist.models import TodoList

# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task