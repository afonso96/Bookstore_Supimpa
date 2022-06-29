from rest_framework import routers
from .views import StockViewSet


stock_router = routers.DefaultRouter()
stock_router.register("stock", viewset=StockViewSet, basename="stock")
