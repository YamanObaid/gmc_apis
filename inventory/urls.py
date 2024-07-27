from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, InventoryViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet, basename='warehouses')
router.register(r'category', CategoryViewSet, basename='category')
urlpatterns = [
    path('', include(router.urls)),
    path('warehouses/id/<int:warehouse_id>/', WarehouseViewSet.as_view({'get': 'retrieve'}), name='warehouse-detail-id'),
    path('category/id/<int:category_id>/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category-detail-id'),
    path('inventory/', InventoryViewSet.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryViewSet.as_view(), name='inventory-detail'),
]
