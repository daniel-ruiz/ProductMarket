from django.contrib import admin
from products.models import Category, Subcategory, Product

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
