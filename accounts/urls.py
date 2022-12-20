from django.urls import path
from .views import SignUpView, PasswordResetView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', SignUpView.as_view(), name='login'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
]
