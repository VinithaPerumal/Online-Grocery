# Generated by Django 4.1.3 on 2022-11-27 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productpage', '0006_remove_item_id_item_itemid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemID',
        ),
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, default=65, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]