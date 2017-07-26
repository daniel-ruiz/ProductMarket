from products.models import Category, Product, Subcategory


class CategoryManager:

    @staticmethod
    def all():
        return Category.objects.all()


class SubcategoryManager:

    @staticmethod
    def all_names():
        return Subcategory.objects.values_list('name', flat=True)

    @staticmethod
    def with_names(names):
        return Subcategory.objects.filter(name__in=names)


class ProductManager:

    @staticmethod
    def all():
        return Product.objects.all()
