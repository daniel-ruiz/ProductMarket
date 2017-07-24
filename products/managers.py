from products.models import Category


class CategoryManager:

    @staticmethod
    def all():
        return Category.objects.all()
