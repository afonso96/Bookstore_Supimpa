import pytest
from django.test import Client
from books.models import Books

def test_create_book_without_arguments_should_succeed(client) -> None:
    pass