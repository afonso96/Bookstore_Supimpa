from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Books
from .serializers import BookSerializers


class BooksViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Books.objects.all().order_by("author")
    pagination_class = PageNumberPagination
