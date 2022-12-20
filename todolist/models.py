from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=255)
    # todoitems = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    icon_color = models.CharField('icon color', max_length=255, null=True, blank=True, default="#d848d6")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail-todolist', kwargs={'pk', self.pk})