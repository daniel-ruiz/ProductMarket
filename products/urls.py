from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from products.api import CategoryListAPI, ProductAPI, SubcategoryProductsAPI

router = DefaultRouter()
router.register(r'products', ProductAPI, base_name='product')

urlpatterns = [
    url(r'^categories/$', CategoryListAPI.as_view()),
    url(r'^categories/(?P<pk>\d+)/products/$', SubcategoryProductsAPI.as_view()),
    url(r'', include(router.urls))
]
