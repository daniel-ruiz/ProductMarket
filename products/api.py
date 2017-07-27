from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.managers import CategoryManager, ProductManager, SubcategoryManager
from products.pagination import ProductMarketPagination
from products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPI(ListAPIView):

    queryset = CategoryManager.all()
    serializer_class = CategorySerializer
    pagination_class = ProductMarketPagination


class ProductAPI(ModelViewSet):

    queryset = ProductManager.all()
    serializer_class = ProductSerializer
    pagination_class = ProductMarketPagination


@api_view()
def list_products_related_to_subcategory(request, pk):
    subcategory = get_object_or_404(SubcategoryManager.all(), pk=pk)
    paginator = ProductMarketPagination()
    paginated_data = paginator.paginate_queryset(subcategory.product_set.all(), request)
    serializer = ProductSerializer(paginated_data, many=True)
    return paginator.get_paginated_response(serializer.data)
