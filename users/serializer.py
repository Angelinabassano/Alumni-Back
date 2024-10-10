from rest_framework import serializers
from .models import User


class RPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'school', 'email', 'password']


class CoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'school', 'rp', 'linkedin', 'github', 'email', 'password']


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['company_name', 'nif', 'email', 'password', 'phone', 'website']
