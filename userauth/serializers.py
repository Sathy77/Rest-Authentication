from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer (serializers.ModelSerializer):
    super_user = serializers.BooleanField(required=False) #super_user custome made
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active', 'is_staff', 'super_user']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data.get('super_user', False): #super_user true then create a super_user
            user = User.objects.create_superuser(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], is_active=True, is_staff=True)
        else:                                       #ortherwise create a normal user
            user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        # user.set_password(validated_data['password'])
        # user.save()
        return user