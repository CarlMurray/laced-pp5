# Generated by Django 4.2.4 on 2024-01-07 18:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_order_orderaddress_orderitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderaddress",
            name="useraddress_ptr",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="item",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="order",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderAddress",
        ),
        migrations.DeleteModel(
            name="OrderItem",
        ),
    ]