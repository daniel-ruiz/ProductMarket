from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(Category):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
