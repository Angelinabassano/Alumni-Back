from rest_framework import serializers
from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'logo', 'company', 'created_at', 'updated_at']
        read_only_fields = ['company', 'created_at', 'updated_at']
