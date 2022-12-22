from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View, FormView
# from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


# Create your views here.
# class LoginView(CreateView):
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('todolist:list-todolist')
#     form_class = UserCreationForm

class LoginUser(LoginView):
    fields = '__all__'
    template_name = 'registration/login.html'
    success_url = reverse_lazy('todolist:list-todolist')
    redirect_authenticated_user = True
    # def get(self, request):
    #     return render(request, 'registration/login.html')
        
    # def post(self, request):
    #     username = request.user.username
    #     password = request.user.password
    #     user = authenticate(username, password)
        
    #     if user is not None:
    #         login(request, user)

class SignUpUser(FormView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')
    redirect_authenticated_users= True
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            return redirect('accounts:login')
        else:
            return redirect('accounts:signup')
    
class PasswordResetView(UpdateView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('accounts:login')
    form_class = PasswordResetForm