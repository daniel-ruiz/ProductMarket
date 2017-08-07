from django.db import models

from products import managers


class NamedResource(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(NamedResource):

    objects = managers.CategoryManager()

    class Meta:
        verbose_name_plural = 'categories'


class Subcategory(NamedResource):

    objects = managers.SubcategoryManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name_plural = 'subcategories'


class Product(NamedResource):

    objects = managers.ProductManager()
    subcategories = models.ManyToManyField(Subcategory)
