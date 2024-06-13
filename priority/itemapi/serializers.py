from rest_framework import serializers
from supplierapi.serializers import SupplierSerializer

from .models import Item


class ItemSerializer(
    serializers.ModelSerializer):
    suppliers = SupplierSerializer(
        many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
