from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Books, Author, Genre
from .serializers import BookSerializers, AuthorSerializers, GenreSerializers


class BooksViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Books.objects.all().order_by("author")
    pagination_class = PageNumberPagination


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()
    pagination_class = PageNumberPagination


class GenreViewSets(ModelViewSet):
    serializer_class = GenreSerializers
    queryset = Genre.objects.all()
    pagination_class = PageNumberPagination
