from django.contrib import admin
from .models import *


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductVariantInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderAddress)
