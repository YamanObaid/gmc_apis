# Generated by Django 5.0.7 on 2024-07-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_product_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='warehouse_code',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
