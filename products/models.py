from django.db import models
from django.db.models import fields


class Category(models.Model):
    name = fields.CharField(max_length=60, blank=False, null=False, unique=True)
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
