from app.gallery.views import GalleryListView, GalleryDetailView
from django.urls import path
from app.user.views import ChangePasswordView, ProfileView, RegisterView

users = [
    path('register', RegisterView.as_view(), name='register'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('profile', ProfileView.as_view(), name='profile'),
]

gallery = [
    path('gallery', GalleryListView.as_view()),
    path('gallery/<int:pk>', GalleryDetailView.as_view()),
]

urlpatterns = users + gallery
