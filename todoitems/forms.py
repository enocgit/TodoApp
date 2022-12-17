from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    # task = forms.CharField(widget=forms.TextInput, label='')
    class Meta:
        model = TodoItem
        # fields = '__all__'
        fields = ['task']
        labels = {
            'task': ''
        }
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control' })
        }

# form = TodoItemForm()