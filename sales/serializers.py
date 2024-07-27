from rest_framework import serializers
from .models import sales_customer, sales_op

class Sales_customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales_customer
        fields = '__all__'

class Sales_opSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales_op
        fields = '__all__'