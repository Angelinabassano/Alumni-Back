class RPValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        required_fields = ['first_name', 'last_name', 'email', 'password']
        for field in required_fields:
            if not self.data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio para RP")


class CoderValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        required_fields = ['first_name', 'last_name', 'email', 'password', 'rp']
        for field in required_fields:
            if not self.data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio para Coder")


class EmpresaValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        required_fields = ['company_name', 'nif', 'email', 'password']
        for field in required_fields:
            if not self.data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio para Empresa")
