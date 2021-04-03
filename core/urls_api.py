from django.urls import path
from app.users.views import ChangePasswordView, ProfileView, RegisterView

users = [
    path('register', RegisterView.as_view(), name='register'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('profile', ProfileView.as_view(), name='profile'),
]

urlpatterns = users
