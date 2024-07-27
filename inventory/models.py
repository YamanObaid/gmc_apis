from django.db import models


class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_code = models.CharField(unique=True, max_length=100, default='')
    category_father = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'category'

class warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=100)
    warehouse_code = models.CharField(unique=True, default='',max_length=100 )

    def __str__(self):
        return self.warehouse_name
    
    class Meta:
        db_table = 'warehouse'

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_code = models.IntegerField(default=0)
    product_name = models.CharField(max_length=255, default='default name')
    product_unit = models.CharField(max_length=100, default='unit')
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    product_price = models.FloatField()
    warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'product'




class inventory(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    

    def __INT__(self):
        return self.product_id
    
    class Meta:
        db_table = 'inventory'


class transfer(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    from_warehouse = models.ForeignKey(warehouse, related_name='from_warehouse', on_delete=models.CASCADE)
    to_warehouse = models.ForeignKey(warehouse, related_name='to_warehouse', on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.CharField(max_length=255)

    def __str__(self):
        return self.transfer_id
    
    class Meta:
        db_table = 'transfer'

class transfer_detail(models.Model):
    transfer = models.ForeignKey(transfer, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return f'{self.transfer_id} - {self.product_id}'
    
    class Meta:
        db_table = 'transfer_detail'