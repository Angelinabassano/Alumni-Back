from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RPSerializer, CoderSerializer, EmpresaSerializer
from .validators import RPValidator, CoderValidator, EmpresaValidator


class UserCreateView(APIView):
    def POST(self, request):
        role = request.data.get('role')

        if role == 'rp':
            validator = RPValidator(request.data)
            validator.validate()
            serializer = RPSerializer(data=request.data)
        elif role == 'coder':
            validator = CoderValidator(request.data)
            validator.validate()
            serializer = CoderSerializer(data=request.data)
        elif role == 'empresa':
            validator = EmpresaValidator(request.data)
            validator.validate()
            serializer = EmpresaSerializer(data=request.data)
        else:
            return Response({'error': 'Rol no válido'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
