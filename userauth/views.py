from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken
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

