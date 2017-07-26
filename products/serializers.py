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

    def validate_subcategories(self, value):
        if value is None or len(value) == 0:
            raise serializers.ValidationError('A product must be related to at least one existing subcategory')

        subcategory_names = SubcategoryManager.all_names()

        for subcategory_data in value:
            subcategory_name = subcategory_data.get('name')
            if subcategory_name not in subcategory_names:
                raise serializers.ValidationError(
                    'The provided subcategory name "{subcategory_name}" does not match any of the existing '
                    'subcategory names'.format(subcategory_name=subcategory_name)
                )

        return value

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
