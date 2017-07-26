from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.managers import CategoryManager, ProductManager, SubcategoryManager
from products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPI(ListAPIView):

    queryset = CategoryManager.all()
    serializer_class = CategorySerializer


class ProductAPI(ModelViewSet):

    queryset = ProductManager.all()
    serializer_class = ProductSerializer


@api_view()
def list_products_related_to_subcategory(request, pk):
    subcategory = get_object_or_404(SubcategoryManager.all(), pk=pk)
    serializer = ProductSerializer(subcategory.product_set, many=True)
    return Response(serializer.data)
