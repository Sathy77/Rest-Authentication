from django.db import models
from teacher.choice import choices
from django.contrib.auth.models import User

# Create your models here.
class Teacher (models.Model):
    name = models.CharField(max_length= 100, blank=True, null=True)
    tid = models.CharField(max_length= 10, blank=True, null=True)
    gender = models.CharField(max_length= 10, choices=choices.GENDER, blank=True, null=True)
    distric = models.CharField(max_length= 20, choices=choices.DISTRICTS, blank=True, null=True)
    userinfo = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.userinfo.username}'
