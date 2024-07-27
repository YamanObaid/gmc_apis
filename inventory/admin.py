from django.contrib import admin

# Register your models here.
from .models import product, warehouse, category, inventory, transfer, transfer_detail

admin.site.register(product)
admin.site.register(warehouse)
admin.site.register(category)
admin.site.register(inventory)
admin.site.register(transfer)
admin.site.register(transfer_detail)