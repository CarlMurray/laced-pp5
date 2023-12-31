# Generated by Django 4.2.4 on 2023-09-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(default=False, verbose_name="Featured Product?"),
        ),
        migrations.AddField(
            model_name="product",
            name="sale_price",
            field=models.DecimalField(decimal_places=2, default=False, max_digits=10),
        ),
    ]
