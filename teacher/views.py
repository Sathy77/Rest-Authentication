from teacher.serializer.serializers import TeacherSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from teacher.models import Teacher
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTeachers(request):
    teacher = Teacher.objects.all()
    teacherserializer=TeacherSerializer(teacher, many=True)
    return Response(teacherserializer.data)
