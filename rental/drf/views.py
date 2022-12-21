from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rental.drf.serializer import AllProducts, ProductInventorySerializer
from rental.inventory.models import Product, ProductInventory


class AllProductsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
