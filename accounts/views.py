from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
# from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


# Create your views here.
# class LoginView(CreateView):
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('todolist:list-todolist')
#     form_class = UserCreationForm

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    
class PasswordResetView(UpdateView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('login')
    form_class = PasswordResetForm