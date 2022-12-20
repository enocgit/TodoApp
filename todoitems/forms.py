from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    # task = forms.CharField(widget=forms.TextInput, label='')
    class Meta:
        model = TodoItem
        # fields = '__all__'
        fields = ['task', 'todolist']
        labels = {
            'task': '',
            'todolist': 'Choose association group'
        }
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control' }),
            'todolist': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
class TodoItemUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['task']
        labels = {
            'task': ''
        }
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'})
        }
        

class LoginForm(auth_forms.AuthenticationForm):
    # class Meta:
    #     model = User
    #     # fields = ['username', 'password']
        
    #     labels = {
    #         'username': '',
    #         'password': '',
    #     }        
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control'}),
    #         'password': forms.TextInput(attrs={'class': 'form-control'}),
    #     }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
        {'class': 'form-control'}
        )


# form = LoginForm()