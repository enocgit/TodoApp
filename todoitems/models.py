from django.db import models
from todolist.models import TodoList
from django.urls import reverse

# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    todolist = models.ForeignKey(TodoList, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
    
    def get_absolute_url(self):
        return reverse("detail-todolist", kwargs={"pk": self.pk})
    

    