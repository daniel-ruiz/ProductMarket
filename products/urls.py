from django.conf.urls import url

from products.api import CategoryListAPI

urlpatterns = [
    url(r'^categories/$', CategoryListAPI.as_view())
]
