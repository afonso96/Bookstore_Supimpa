from rest_framework import routers

from .views import BooksViewSet, AuthorViewSet, GenreViewSets

books_router = routers.DefaultRouter()
books_router.register("books", viewset=BooksViewSet, basename="books")
books_router.register("authors", viewset=AuthorViewSet, basename="authors")
books_router.register("genero", viewset=GenreViewSets, basename="genero")
