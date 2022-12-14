from django.contrib import admin
from rental.inventory.models import Product, ProductInventory, Brand, ProductType
from django.template.defaultfilters import truncatechars


def short_description(self):
    return truncatechars(self.description, 35)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'web_id', 'short_description',
                    'slug', 'is_active']
    search_fields = ['name', 'description', 'web_id', ]
    list_per_page = 10
    list_filter = ['name', 'created_at']

    def short_description(self, obj):
        return obj.description[:50]


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'upc', 'product', 'sku',
                    'store_price', 'sale_price', 'weight']
    search_fields = ['product', 'store_price', 'sale_price', ]
    list_per_page = 10
    list_filter = ['product', 'created_at']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']
    search_fields = ['name', ]
    list_per_page = 10
    list_filter = ['name']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']
    search_fields = ['name', ]
    list_per_page = 10
    list_filter = ['name']
