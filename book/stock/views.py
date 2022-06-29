from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import StockSerializers
from .models import Stock


class StockViewSet(ModelViewSet):
    serializer_class = StockSerializers
    queryset = Stock.objects.all()
    pagination_class = PageNumberPagination
