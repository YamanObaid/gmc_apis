# Generated by Django 5.0.6 on 2024-07-21 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('transfer_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(max_length=100)),
                ('warehouse_code', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_Father_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_code', models.IntegerField(default=0)),
                ('product_name', models.CharField(default='default name', max_length=255)),
                ('product_unit', models.CharField(default='unit', max_length=100)),
                ('product_price', models.FloatField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='TransferDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('transfer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.transfer')),
                ('from_warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='transfer',
            name='from_warehouse_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_warehouse', to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='to_warehouse_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_warehouse', to='inventory.warehouse'),
        ),
    ]