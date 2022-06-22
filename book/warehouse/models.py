from django.db import models


class Warehouse(models.Model):
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    addres = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
