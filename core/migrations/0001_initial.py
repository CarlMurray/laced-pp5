# Generated by Django 4.2.4 on 2023-09-04 07:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Product Name")),
                (
                    "sku",
                    models.CharField(
                        help_text="SKU must be unique and exactly 6 numerical characters",
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="SKU must be exactly 6 numerical characters",
                                regex="[0-9]{6}",
                            )
                        ],
                        verbose_name="SKU",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=500, verbose_name="Product Description"
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="media/", verbose_name="Image")),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="core.productcategory",
            ),
        ),
    ]
