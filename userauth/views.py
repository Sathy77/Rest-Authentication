from rest_framework import generics, status, permissions             #permissions only for login
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer #only for login
from knox.views import LoginView as KnoxLoginView                    #only for login
from django.contrib.auth import login                                #only for login

from userauth.serializers import RegisterSerializer

# Create your views here.
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() 
        return Response({
            # 'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'user': request.data['username'],
            'token': AuthToken.objects.create(user)[1]
        }, status=status.HTTP_201_CREATED)
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

