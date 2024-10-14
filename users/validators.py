from rest_framework import serializers
from .models import User


class RPValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        required_fields = ['first_name', 'last_name', 'email', 'password']
        for field in required_fields:
            if not self.data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio para RP")

        if 'email' in self.data and not self.data['email'].count('@') == 1:
            raise serializers.ValidationError("El campo 'email' no tiene un formato válido")


class CoderValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        required_fields = ['first_name', 'last_name', 'email', 'password', 'rp']
        for field in required_fields:
            if not self.data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio para Coder")

        if 'rp' in self.data and not self.is_valid_rp(self.data['rp']):
            raise serializers.ValidationError("El RP proporcionado no es válido o no existe")

        if 'email' in self.data and not self.data['email'].count('@') == 1:
            raise serializers.ValidationError("El campo 'email' no tiene un formato válido")

    def is_valid_rp(self, rp_id):
        try:
            rp = User.objects.get(id=rp_id, role='rp')
            return True
        except User.DoesNotExist:
            return False


class EmpresaValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        required_fields = ['company_name', 'nif', 'email', 'password']
        for field in required_fields:
            if not self.data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio para Empresa")

        if 'nif' in self.data and not self.is_valid_nif(self.data['nif']):
            raise serializers.ValidationError("El N.I.F proporcionado no tiene un formato válido o ya está en uso")

        if 'email' in self.data and not self.data['email'].count('@') == 1:
            raise serializers.ValidationError("El campo 'email' no tiene un formato válido")

    def is_valid_nif(self, nif):
        if len(nif) == 9:
            if nif[0].isalpha() and nif[1:].isdigit():
                return True
        return False

