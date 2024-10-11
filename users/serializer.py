from rest_framework import serializers
from .models import User


class RPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'school', 'role']

    def validate(self, data):
        if 'rp' not in data['role']:
            raise serializers.ValidationError('El rol debe ser "rp"')
        return data


class CoderSerializer(serializers.ModelSerializer):
    rp = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='rp'))  # Relacionar con RP

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'rp', 'role']

    def validate(self, data):
        if 'coder' not in data['role']:
            raise serializers.ValidationError('El rol debe ser "coder"')
        return data


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['company_name', 'nif', 'email', 'password', 'role']

    def validate(self, data):
        if 'empresa' not in data['role']:
            raise serializers.ValidationError('El rol debe ser "empresa"')
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
