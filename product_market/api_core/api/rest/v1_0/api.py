from django.conf.urls import url, include

urlpatterns = [
    url(
        r'',
        include('products.api.rest.v1_0.api_urls')
    )
]
