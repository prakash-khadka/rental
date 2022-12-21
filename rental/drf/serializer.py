from rest_framework import serializers
from rental.inventory.models import Product, ProductInventory


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False
        depth = 2


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only = True
        depth = 2
