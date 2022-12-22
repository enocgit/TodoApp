from django.forms import ModelForm
from .models import TodoList


class CreateListForm(ModelForm):
    
    class Meta:
        model = TodoList
        fields = '__all__'