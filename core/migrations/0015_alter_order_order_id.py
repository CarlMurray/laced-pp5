# Generated by Django 4.2.4 on 2024-01-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0014_alter_order_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_id",
            field=models.CharField(),
        ),
    ]