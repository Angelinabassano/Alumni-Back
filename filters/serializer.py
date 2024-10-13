from rest_framework import serializers
from .models import Coder

class CoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coder
        fields = '__all__'
