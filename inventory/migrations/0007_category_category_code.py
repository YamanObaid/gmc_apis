# Generated by Django 5.0.7 on 2024-07-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_warehouse_warehouse_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_code',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
