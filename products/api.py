from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from products.managers import CategoryManager, ProductManager, SubcategoryManager
from products.pagination import ProductMarketPagination
from products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPI(ListAPIView):

    queryset = CategoryManager.all()
    serializer_class = CategorySerializer
    pagination_class = ProductMarketPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'updated_at')


class ProductAPI(ModelViewSet):

    queryset = ProductManager.all()
    serializer_class = ProductSerializer
    pagination_class = ProductMarketPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'updated_at')


@api_view()
def list_products_related_to_subcategory(request, pk):
    subcategory = get_object_or_404(SubcategoryManager.all(), pk=pk)
    filtered_queryset = SearchFilter().filter_queryset(request, subcategory.product_set.all(), view=list_products_related_to_subcategory)
    filtered_queryset = OrderingFilter().filter_queryset(request, filtered_queryset, view=list_products_related_to_subcategory)
    paginator = ProductMarketPagination()
    paginated_data = paginator.paginate_queryset(filtered_queryset, request)
    serializer = ProductSerializer(paginated_data, many=True)
    return paginator.get_paginated_response(serializer.data)

list_products_related_to_subcategory.search_fields = ('name',)
list_products_related_to_subcategory.ordering_fields = ('name', 'created_at', 'updated_at')
