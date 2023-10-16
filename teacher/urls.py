from django.urls import path
from teacher.views import  getTeachers

urlpatterns = [
    path('get-teachers/', getTeachers, name='get-teachers'),
]