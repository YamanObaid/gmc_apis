from django.contrib import admin
from .models import sales_customer, sales_op

# Register your models here.
admin.site.register(sales_customer)
admin.site.register(sales_op)