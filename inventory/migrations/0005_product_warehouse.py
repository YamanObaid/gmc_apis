# Generated by Django 5.0.7 on 2024-07-21 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_rename_transferdetail_transfer_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
        ),
    ]
