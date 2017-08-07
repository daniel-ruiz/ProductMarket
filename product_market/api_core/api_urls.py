from django.conf.urls import url, include

urlpatterns = [
    url(
        r'rest/v1_0/',
        include('product_market.api_core.api.rest.v1_0.api')
    )
]
