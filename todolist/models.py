from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=255)
    # todoitems = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    icon_color = models.CharField('icon color', max_length=255, null=True, blank=True, default="#d848d6")
    
    def __str__(self):
        return self.name