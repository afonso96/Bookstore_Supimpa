from rest_framework import serializers
from .models import Books


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["id", "titulo", "author", "ano", "genero", "price", "visible"]
