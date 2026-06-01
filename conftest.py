import pytest
from main import BooksCollector

@pytest.fixture()
def books():
    books = BooksCollector()
    books.add_new_book('Дюна')
    books.add_new_book('Шерлок Холмс')
    return books

