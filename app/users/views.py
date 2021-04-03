from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
# Create your views here.
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, allow_blank=True, validators=[validate_password])

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'is_active',
            'is_staff',
            'last_login',
            'is_superuser',
            'user_permissions',
            'groups',
            'date_joined',
        )
    
    def save(self, **kwargs):
        self.validated_data['password'] = make_password(self.validated_data.get('password'))
        return super().save(**kwargs)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer