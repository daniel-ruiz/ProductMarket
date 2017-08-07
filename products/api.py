from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from products.pagination import ProductMarketPagination
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Subcategory, Product


class CategoryListAPI(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductMarketPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'updated_at')


class ProductAPI(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductMarketPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'updated_at')


class SubcategoryProductsAPI(APIView):

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'updated_at')

    def get(self, request, pk):
        subcategory = get_object_or_404(Subcategory.objects.all(), pk=pk)
        filtered_queryset = self.filter_queryset(subcategory.product_set.all())
        paginator = ProductMarketPagination()
        paginated_data = paginator.paginate_queryset(filtered_queryset, request)
        serializer = ProductSerializer(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def filter_queryset(self, query_set):
        for backend in self.filter_backends:
            query_set = backend().filter_queryset(self.request, query_set, view=self)
        return query_set
