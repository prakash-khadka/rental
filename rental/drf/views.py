from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rental.drf.serializer import AllProducts, ProductInventorySerializer
from rental.inventory.models import Product, ProductInventory
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.http import HttpResponse
from elasticsearch_dsl import Q

# from ecommerce.drf.serializer import ProductInventorySerializer
from rental.inventory.documents import ProductInventoryDocument


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


class SearchProductInventory(APIView, LimitOffsetPagination):
    productinventory_serializer = ProductInventorySerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'product.name'
                ], fuzziness='auto') & Q(
                    'bool',
                        should=[
                            Q('match', is_default=True),
                        ], minimum_should_match=1)

            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.productinventory_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)
