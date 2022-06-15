from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Books
from .serializers import BookSerializers


class BooksViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Books.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
