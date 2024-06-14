# Generated by Django 5.0.6 on 2024-06-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemapi', '0004_remove_item_suppliers'),
        ('supplierapi', '0003_remove_supplier_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='items',
            field=models.ManyToManyField(related_name='items', to='itemapi.item'),
        ),
    ]
