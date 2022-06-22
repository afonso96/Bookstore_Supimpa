from rest_framework import serializers
from .models import Books, Author, Genre


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["id", "title", "author", "year", "genre", "price", "visible"]


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "author"]


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre"]