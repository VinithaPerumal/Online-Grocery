# Generated by Django 4.1.3 on 2022-11-27 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productpage', '0010_customer_order_order_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='order_items',
            new_name='order_item',
        ),
    ]