from django.contrib import admin
from rental.inventory.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'web_id', 'description',
                    'slug', 'is_active']
    search_fields = ['name', 'description', 'web_id', ]
    list_per_page = 20
    list_filter = ['name', 'created_at']

