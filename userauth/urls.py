from django.urls import path
from userauth.views import RegisterAPI, LoginAPI
from knox import views as knox_views  #use for only longout

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'), #logout 
]