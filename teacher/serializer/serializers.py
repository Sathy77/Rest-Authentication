from rest_framework import serializers
from django.contrib.auth.models import User
from userauth.serializers import UserSerializers
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    userinfo = UserSerializers(many=False)
    class Meta:
        model = Teacher
        fields = '__all__'

