# inventory/serializers.py

from rest_framework import serializers
from .models import warehouse, inventory, category


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = warehouse
        fields = ['warehouse_id', 'warehouse_name', 'warehouse_code']


class DynamicInventorySerializer(serializers.Serializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    def to_internal_value(self, data):
        return super().to_internal_value(data)
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['category_id', 'category_name', 'category_code', 'category_father_id']