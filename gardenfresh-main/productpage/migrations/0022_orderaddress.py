# Generated by Django 4.1.3 on 2022-11-30 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productpage', '0021_alter_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phno', models.TextField(max_length=10)),
                ('address', models.TextField()),
                ('PIN', models.TextField()),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productpage.order')),
            ],
        ),
    ]
