from django.db import models

# Create your models here.
class sales_customer (models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100, default='')
    shop_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    tel_number = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=100, null=True)
    governate = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    client_activity_old = models.CharField(max_length=100, null=True)
    shop_status = models.CharField(max_length=100, null=True)
    responsible = models.CharField(max_length=100, null=True)
    customer_size = models.IntegerField(null=True, default=0)
    client_place_of_birth = models.CharField(max_length=100, null=True)
    client_date_of_birth = models.CharField(max_length=100, null=True)
    client_marital_status = models.CharField(max_length=100, null=True)
    client_number_of_children = models.IntegerField(null=True, default = 0)
    shop_space = models.CharField(max_length=100, null=True)
    number_of_warehouses = models.IntegerField(default=0, null=True)
    number_of_workers = models.IntegerField(default=0, null=True)
    notes = models.CharField(max_length=150, null=True)
    static_discount = models.CharField(max_length=100, null=True)
    month_discount = models.CharField(max_length=100, null=True)
    year_discount = models.CharField(max_length=100, null=True)
    gift_on_quantity = models.CharField(max_length=100, null=True)
    gift_on_value = models.CharField(max_length=100, null=True)
    client_trade_type = models.CharField(max_length=100, null=True)
    client_location_within_region = models.IntegerField(default=0, null=True)
    client_locations_within_governate = models.IntegerField(default=0, null=True)
    client_locations_oustide_governate = models.IntegerField(default=0, null=True)
    paint_proffession = models.CharField(max_length=100, null=True)
    dependence_on_company = models.CharField(max_length=100, null=True)
    cred_finance = models.CharField(max_length=100, null=True)
    cred_deals = models.CharField(max_length=100, null=True)
    cred_complains = models.CharField(max_length=100, null=True)
    method_cash = models.BooleanField(null=True)
    method_payments = models.BooleanField(null=True)
    method_offers = models.BooleanField(null=True)
    method_custody = models.BooleanField(null=True)
    activity_paints = models.BooleanField(null=True)
    activity_plumping = models.BooleanField(null=True)
    activity_electrical = models.BooleanField(null=True)
    activity_haberdashery = models.BooleanField(null=True)
    special_items_oil = models.CharField(max_length=100, null=True)
    special_items_water = models.CharField(max_length=100, null=True)
    special_items_acrylic = models.CharField(max_length=100, null=True)
    gmc_percentage = models.FloatField(default=0, null=True)
    bzreh_percentage = models.FloatField(default=0, null=True)
    bermoglez_percentage = models.FloatField(default=0, null=True)
    alksasas_percentage = models.FloatField(default=0, null=True)
    al42_percentage = models.FloatField(default=0, null=True)
    alharash_percentage = models.FloatField(default=0, null=True)
    ocean_percentage = models.FloatField(default=0, null=True)
    alhafez_percentage = models.FloatField(default=0, null=True)
    bentol_percentage = models.FloatField(default=0, null=True)
    albatrek_percentage = models.FloatField(default=0, null=True)
    upco_percentage = models.FloatField(default=0, null=True)
    spider_percentage = models.FloatField(default=0, null=True)
    terget_percentage = models.FloatField(default=0, null=True)
    other_percentage = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.customer_name
    
    class Meta:
        db_table = 'sales_customer'

class sales_op (models.Model):
    sales_op_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(sales_customer, on_delete=models.SET_NULL, null = True)
    operation_type = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(max_length=100, null=True)
    operator_1 = models.CharField(max_length=100, null=True)
    operator_2 = models.CharField(max_length=100, null=True)
    process_kind = models.CharField(max_length=100, null=True)
    connection_type = models.CharField(max_length=100, null=True)
    reception = models.CharField(max_length=100, null=True)
    discussion = models.CharField(max_length=100, null=True)
    social_talk = models.BooleanField(max_length=100, null=True)
    business_talk = models.BooleanField(max_length=100, null=True)
    bill = models.BooleanField(max_length=100, null=True)
    complaints = models.BooleanField(max_length=100, null=True)
    selling_paints = models.CharField(max_length=100, null=True)
    payed_money = models.BooleanField(max_length=100, null=True)
    changes_of_shop = models.BooleanField(max_length=100, null=True)
    selling_others = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.operation_type
    
    class Meta:
        db_table = 'sales_op'