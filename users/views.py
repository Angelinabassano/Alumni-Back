from users.serializer import RPCreateSerializer, CoderCreateSerializer, EmpresaCreateSerializer, RPUpdateSerializer, \
    CoderUpdateSerializer, EmpresaUpdateSerializer
from users.validators import RPValidator, CoderValidator, EmpresaValidator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from users.models import User


class UserCreateView(APIView):
    def post(self, request):
        role = request.data.get('role')
        serializer = None
        validator = None

        if role == 'rp':
            serializer = RPCreateSerializer(data=request.data)
            validator = RPValidator(request.data)
        elif role == 'coder':
            serializer = CoderCreateSerializer(data=request.data)
            validator = CoderValidator(request.data)
        elif role == 'empresa':
            serializer = EmpresaCreateSerializer(data=request.data)
            validator = EmpresaValidator(request.data)
        else:
            return Response({'error': 'Rol no válido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validator.validate()
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

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
