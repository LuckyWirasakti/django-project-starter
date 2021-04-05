from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, allow_blank=True, validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
            'date_joined',
        )
        read_only_fields = (
            'is_active',
            'last_login',
            'date_joined',
        )
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'date_joined',
        )
        read_only_fields = (
            'id',
            'username',
            'date_joined',
        )

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True, validators=[validate_password])
    class Meta:        
        model = User
        fields = (
            'password',
        )
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)