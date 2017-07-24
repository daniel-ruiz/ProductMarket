from products.models import Category, Product


class CategoryManager:

    @staticmethod
    def all():
        return Category.objects.all()


class ProductManager:

    @staticmethod
    def all():
        return Product.objects.all()
