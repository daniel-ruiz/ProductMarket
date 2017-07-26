from products.managers import SubcategoryManager
from products.models import Category, Subcategory, Product
from rest_framework import serializers


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        exclude = ('category',)
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {
                'validators': []
            }
        }


class CategorySerializer(serializers.ModelSerializer):

    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'subcategories')


class ProductSerializer(serializers.ModelSerializer):

    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
