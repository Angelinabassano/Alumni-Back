from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RPSerializer, CoderSerializer, EmpresaSerializer
from .validators import RPValidator, CoderValidator, EmpresaValidator


class UserCreateView(APIView):
    def post(self, request):
        role = request.data.get('role')

        if role == 'rp':
            serializer = RPSerializer(data=request.data)
            validator = RPValidator(request.data)
        elif role == 'coder':
            serializer = CoderSerializer(data=request.data)
            validator = CoderValidator(request.data)
        elif role == 'empresa':
            serializer = EmpresaSerializer(data=request.data)
            validator = EmpresaValidator(request.data)
        else:
            return Response({'error': 'Rol no válido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validator.validate()
        except serializer.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)