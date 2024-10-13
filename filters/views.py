from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Coder
from .filters import CoderFilter
from .serializers import CoderSerializer


class CoderListView(generics.ListAPIView):
    queryset = Coder.objects.all()
    serializer_class = CoderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CoderFilter
