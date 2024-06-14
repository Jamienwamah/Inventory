from django.db import models
from itemapi.models import Item


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    items = models.ManyToManyField(
        Item, related_name='items')

    def __str__(self):
        return self.name

