from rest_framework import routers

from .views import BooksViewSet

books_router = routers.DefaultRouter()
books_router.register("books", viewset=BooksViewSet, basename="books")
