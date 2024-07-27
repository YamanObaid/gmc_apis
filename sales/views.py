from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import sales_customer, sales_op
from .serializers import Sales_customerSerializer, Sales_opSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

class SalesCustomerViewSet(viewsets.ModelViewSet):
    queryset = sales_customer.objects.all()
    serializer_class = Sales_customerSerializer
    permission_classes = [IsAuthenticated]

    def list (self, request, *args, **kwargs):
        search_keyword = request.query_params.get('search', None)
        if search_keyword:
            queryset = self.queryset.filter(
                Q(customer_name__icontains=search_keyword) |
                Q(shop_name__icontains=search_keyword)
            )
        else:
            queryset = sales_customer.objects.all()
        
        if not queryset.exists():
            return Response({"detail": "No customer matches the given query."},status=404)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        if 'customer_id' in self.kwargs:
            lookup_field = 'customer_id'
            lookkup_value = self.kwargs['customer_id']
            obj = get_object_or_404(self.queryset, **{lookup_field: lookkup_value})
            serializer = self.get_serializer(obj)
            return Response (serializer.data)
        return Response ({"detail":"No customer matches the given query."}, status=404)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        self.perform_update(serializer.data)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response([{"detail": "customer deleted."}],status=status.HTTP_200_OK)

""""""

class SalesOpsViewSet(viewsets.ModelViewSet):
    queryset = sales_op.objects.all()
    serializer_class = Sales_opSerializer
    permission_classes = [IsAuthenticated]

    def list (self, request, *args, **kwargs):
        search_keyword = request.query_params.get('search', None)
        if search_keyword:
            queryset = self.queryset.filter(
                Q(customer_name__icontains=search_keyword) |
                Q(shop_name__icontains=search_keyword)
            )
        else:
            queryset = sales_op.objects.all()
        
        if not queryset.exists():
            return Response({"detail": "No sales operation matches the given query."},status=404)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        if 'sales_op_id' in self.kwargs:
            lookup_field = 'sales_op_id'
            lookkup_value = self.kwargs['sales_op_id']
            obj = get_object_or_404(self.queryset, **{lookup_field: lookkup_value})
            serializer = self.get_serializer(obj)
            return Response (serializer.data)
        return Response ({"detail":"No sales operation matches the given query."}, status=404)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        self.perform_update(serializer.data)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response([{"detail": "sales operation deleted."}],status=status.HTTP_200_OK)