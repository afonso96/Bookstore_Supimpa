from django.db import models
from django.db import models
from books.models import Books

from warehouse.models import Warehouse


class Stock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=4)
