from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import warehouse,inventory, category
from .serializers import WarehouseSerializer, DynamicInventorySerializer, CategorySerializer
from django.db import connection
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]  # Enforce authentication

    def list(self, request, *args   , **kwargs):
        search_keyword = request.query_params.get('search', None)
        if search_keyword:
            queryset = self.queryset.filter(
                Q(warehouse_name__icontains=search_keyword) |
                Q(warehouse_code__icontains=search_keyword)
            )
        else:
            queryset = warehouse.objects.all()
        
        if not queryset.exists():
            return Response({"detail": "No warehouse matches the given query."}, status=404)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if 'warehouse_id' in self.kwargs:
            lookup_field = 'warehouse_id'
            lookup_value = self.kwargs['warehouse_id']
            obj = get_object_or_404(self.queryset, **{lookup_field: lookup_value})
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        return Response({"detail": "No warehouse matches the given query."}, status=404)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response([{"detail": "warehouse deleted."}],status=status.HTTP_200_OK)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Enforce authentication

    def list(self, request, *args   , **kwargs):
        search_keyword = request.query_params.get('search', None)
        if search_keyword:
            queryset = self.queryset.filter(
 		Q(category_name__icontains=search_keyword) | 
		Q(category_code__icontains=search_keyword))
        else:
            queryset = category.objects.all()
        
        if not queryset.exists():
            return Response({"detail": "No category matches the given query."}, status=404)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if 'category_id' in self.kwargs:
            lookup_field = 'category_id'
            lookup_value = self.kwargs['category_id']
            obj = get_object_or_404(self.queryset, **{lookup_field: lookup_value})
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        return Response({"detail": "No category matches the given query."}, status=404)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response([{"detail": "category deleted."}],status=status.HTTP_200_OK)

"""  """

class InventoryViewSet(APIView):
    permission_classes = [IsAuthenticated]  # Enforce authentication

    def get_columns(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'inventory'")
            columns = [row[0] for row in cursor.fetchall()]
        return columns

    def get(self, request, pk=None, format=None):
        columns = self.get_columns()
        with connection.cursor() as cursor:
            if pk:
                cursor.execute("SELECT * FROM inventory WHERE id = %s", [pk])
                row = cursor.fetchone()
                if not row:
                    return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
                data = dict(zip(columns, row))
            else:
                cursor.execute("SELECT * FROM inventory")
                rows = cursor.fetchall()
                data = [dict(zip(columns, row)) for row in rows]
        return Response(data)

    def post(self, request, format=None):
        columns = self.get_columns()
        data = request.data
        fields = ', '.join(columns)
        values = ', '.join([f"%({col})s" for col in columns if col in data])
        sql = f"INSERT INTO inventory ({fields}) VALUES ({values})"
        with connection.cursor() as cursor:
            cursor.execute(sql, data)
            cursor.execute("SELECT @@IDENTITY")
            pk = cursor.fetchone()[0]
        return self.get(request, pk=pk)

    def put(self, request, pk=None, format=None):
        columns = self.get_columns()
        data = request.data
        set_clause = ', '.join([f"{col} = %({col})s" for col in columns if col in data])
        sql = f"UPDATE inventory SET {set_clause} WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql, {**data, 'id': pk})
        return self.get(request, pk=pk)

    def delete(self, request, pk=None, format=None):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM inventory WHERE id = %s", [pk])
        return Response(status=status.HTTP_204_NO_CONTENT)