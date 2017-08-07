from django.db import models


class CategoryManager(models.Manager):

    def all(self):
        return self.model.objects.all()


class SubcategoryManager(models.Manager):

    def all(self):
        return self.model.objects.all()

    def all_names(self):
        return self.model.objects.values_list('name', flat=True)

    def with_names(self, names):
        return self.model.objects.filter(name__in=names)


class ProductManager(models.Manager):

    def all(self):
        return self.model.objects.all()
