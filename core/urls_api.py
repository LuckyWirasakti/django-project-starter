from django.urls.conf import include, path
from app.users.urls import urlpatterns as urlpatterns_users

urlpatterns = [
]
api = urlpatterns + urlpatterns_users