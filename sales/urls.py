from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesCustomerViewSet, SalesOpsViewSet

router = DefaultRouter()
router.register(r'customer', SalesCustomerViewSet, basename='customer')
router.register(r'salesop', SalesOpsViewSet, basename='salesop')

urlpatterns = [
    path('', include(router.urls)),
    path('customer/id/<int:customer_id>/', SalesCustomerViewSet.as_view({'get': 'retrieve'}), name='customer-detail-id'),
    path('salesop/id/<int:sales_op_id>/', SalesOpsViewSet.as_view({'get': 'retrieve'}), name='salesop-detail-id'),

]

