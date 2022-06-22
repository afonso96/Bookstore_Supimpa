from rest_framework import routers

from .views import WarehouseViewSet

warehouse_router = routers.DefaultRouter()
warehouse_router.register("warehouse", viewset=WarehouseViewSet, basename="warehouse")
