from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from products.managers import CategoryManager, ProductManager
from products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPI(ListAPIView):

    queryset = CategoryManager.all()
    serializer_class = CategorySerializer


class ProductAPI(ModelViewSet):

    queryset = ProductManager.all()
    serializer_class = ProductSerializer
