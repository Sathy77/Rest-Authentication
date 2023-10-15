from django.urls import path
from userauth.views import RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
]