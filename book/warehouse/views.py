from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Warehouse
from .serializers import WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()
    pagination_class = PageNumberPagination
