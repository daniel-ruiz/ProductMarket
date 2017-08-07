from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from products.api.rest.v1_0.api_controllers import CategoryListAPIController, ProductAPIController
from products.api.rest.v1_0.api_controllers import SubcategoryProductsAPIController

router = DefaultRouter()
router.register(r'products', ProductAPIController, base_name='product')

urlpatterns = [
    url(r'categories/$', CategoryListAPIController.as_view()),
    url(r'categories/(?P<pk>\d+)/products/$', SubcategoryProductsAPIController.as_view()),
    url(r'', include(router.urls))
]
