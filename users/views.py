from users.serializer import RPCreateSerializer, CoderCreateSerializer, EmpresaCreateSerializer, RPUpdateSerializer, \
    CoderUpdateSerializer, EmpresaUpdateSerializer, GetCoderSerializer, GetRPSerializer, GetEmpresaSerializer
from users.validators import RPValidator, CoderValidator, EmpresaValidator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status, generics
from users.models import User


class UserCreateView(APIView):
    def post(self, request):
        serializer = None

        if 'company_name' in request.data and 'nif' in request.data:
            serializer = EmpresaCreateSerializer(data=request.data)
        elif 'rp' in request.data:
            serializer = CoderCreateSerializer(data=request.data)
        elif 'school' in request.data:
            serializer = RPCreateSerializer(data=request.data)
        else:
            return Response({'error': 'Datos insuficientes para determinar el rol'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, role):
        try:
            user = User.objects.get(pk=pk, role=role)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        validator = self.get_validator(role, request.data)
        serializer = self.get_serializer(role)(user, data=request.data, partial=True)

        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Usuario actualizado exitosamente'}, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_validator(self, role, data):
        if role == 'rp':
            return RPValidator(data)
        elif role == 'coder':
            return CoderValidator(data)
        elif role == 'empresa':
            return EmpresaValidator(data)
        return None

    def get_serializer(self, role):
        if role == 'rp':
            return RPUpdateSerializer
        elif role == 'coder':
            return CoderUpdateSerializer
        elif role == 'empresa':
            return EmpresaUpdateSerializer
        return None


class CoderListView(generics.ListAPIView):
    queryset = User.objects.filter(role='coder')
    serializer_class = GetCoderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "No hay coders disponibles"}, status=status.HTTP_204_NO_CONTENT)

        fields = request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            serializer = self.get_serializer(queryset, many=True)
            filtered_data = [{field: coder[field] for field in fields if field in coder} for coder in serializer.data]
            return Response(filtered_data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmpresaListView(generics.ListAPIView):
    queryset = User.objects.filter(role='empresa')
    serializer_class = GetEmpresaSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({"detail": "No hay empresas disponibles"}, status=status.HTTP_204_NO_CONTENT)

        fields = request.query_params.get('fields')
        serializer = self.get_serializer(queryset, many=True)

        if fields:
            fields = fields.split(',')
            filtered_data = [{field: empresa[field] for field in fields if field in empresa} for empresa in
                             serializer.data]
            return Response(filtered_data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, role):
        try:
            user = User.objects.get(pk=pk, role=role)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if role == 'rp':
            serializer = GetRPSerializer(user)
        elif role == 'coder':
            serializer = GetCoderSerializer(user)
        elif role == 'empresa':
            serializer = GetEmpresaSerializer(user)
        else:
            return Response({"error": "Rol de usuario no válido"}, status=status.HTTP_400_BAD_REQUEST)

        fields = request.query_params.getlist('fields')
        if fields:
            filtered_data = {field: serializer.data.get(field) for field in fields if field in serializer.data}
            return Response(filtered_data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            role = user.role
            if role not in ['rp', 'coder', 'empresa']:
                return Response({"error": "Rol de usuario no válido"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'role': role,
                'user_id': user.id,
                'email': user.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Correo o contraseña inválidos"}, status=status.HTTP_400_BAD_REQUEST)
