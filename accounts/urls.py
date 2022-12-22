from django.urls import path
from .views import SignUpUser, PasswordResetView, LoginUser
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
]
