from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from products.managers import CategoryManager
from products.serializers import CategorySerializer


class CategoryListAPI(ListAPIView):

    queryset = CategoryManager.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
